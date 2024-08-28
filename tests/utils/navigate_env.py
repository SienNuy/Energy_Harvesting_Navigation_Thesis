import time
import numpy as np
from stable_baselines3.common.vec_env.util import dict_to_obs
from util import sample_start_positions_1robot, sample_start_positions_2robots, sample_start_positions_1robot_small, \
    sample_start_positions_2robots_small


def navigate_my_env(my_env, num_start_positions):
    number_failures = 0
    number_successes = 0

    avg_path_length = 0
    avg_EH = 0
    avg_reward = 0

    path_info = []

    if len(my_env.robots) == 1:
        sample_start_positions = sample_start_positions_1robot
        if my_env.width < 10:
            sample_start_positions = sample_start_positions_1robot_small

    elif len(my_env.robots) == 2:
        sample_start_positions = sample_start_positions_2robots
        if my_env.width < 10:
            sample_start_positions = sample_start_positions_2robots_small

    # Run the model 50 times
    for s in range(num_start_positions):
        my_env.reset()
        start_position = sample_start_positions[s]
        for r in range(len(my_env.robots)):
            my_env.robots[r].reset(start_position[r])

        if len(my_env.robots) == 2:
            path_length = [0, 0]
        else:
            path_length = 0
        reward_ = 0

        if len(path_info) < 11:
            start_positions = [sample_start_positions[s][0]]
            path1 = {0: sample_start_positions[s][0]}
            path2 = {}
            if len(my_env.robots) == 2:
                path2 = {0: sample_start_positions[s][1]}
                start_positions.append(sample_start_positions[s][1])

        # Max 50 steps
        for i in range(50):
            for r, robot in enumerate(my_env.robots):
                if robot.is_done():
                    continue

                # get the best action of the robot based on their q_table
                q_table = robot.q_learn_agent.q_table
                state = robot.position
                q_values = q_table[state]
                best_action = np.argmax(q_values)

                # do the step
                next_state, reward, info = my_env.step(robot, best_action)

                # Check if there is a collision > choose next best action
                if info['causes_collision']:
                    # go on with second best action
                    # Get the indices that would sort the array
                    sorted_indices = np.argsort(q_values)
                    # get second_best_action
                    second_best_action = sorted_indices[-2]
                    next_state, reward, info = my_env.step(robot, second_best_action)
                    print('COLLISION AVOIDANCE')

                reward_ += reward

                if len(my_env.robots) == 2:
                    path_length[r] += 1
                else:
                    path_length += 1

                if len(path_info) < 11:
                    if r == 0:
                        path1[i + 1] = next_state
                    if r == 1:
                        path2[i + 1] = next_state

            if my_env.done():
                number_successes += 1
                if len(my_env.robots) == 2:
                    avg_path_length += (path_length[0] + path_length[1]) / 2
                    avg_EH += (my_env.robots[0].harvested_energy + my_env.robots[1].harvested_energy) / 2
                    path_EH = (my_env.robots[0].harvested_energy + my_env.robots[1].harvested_energy) / 2

                else:
                    avg_path_length += path_length
                    avg_EH += my_env.robots[0].harvested_energy
                    path_EH = my_env.robots[0].harvested_energy
                avg_reward += reward_
                break

        if not my_env.done():
            number_failures += 1

        if len(path_info) < 11:
            p_info = {'start_positions': start_positions, 'gridsize': my_env.width, 'path1': path1, 'path2': path2}
            path_info.append(p_info)

    avg_path_length /= num_start_positions
    avg_reward /= num_start_positions
    avg_EH /= num_start_positions
    print("failures = " + str(number_failures))
    print("successes = " + str(number_successes))
    print("avg path length = " + str(avg_path_length))
    print("avg reward = " + str(avg_reward))
    print("avg EH = " + str(avg_EH))

    # Rounding the floating points to only have 2 decimals
    avg_reward = round(avg_reward, 2)
    avg_EH = round(avg_EH, 2)

    return number_failures, number_successes, avg_path_length, avg_reward, avg_EH, path_info


def navigate_gym_env(gym_env, model, num_robots, gridsize, num_start_positions):
    number_failures = 0
    number_successes = 0

    avg_path_length = 0
    avg_EH = 0
    avg_reward = 0

    path_info = []

    if num_robots == 1:
        sample_start_positions = sample_start_positions_1robot
        if gridsize < 10:
            sample_start_positions = sample_start_positions_1robot_small

    elif num_robots == 2:
        sample_start_positions = sample_start_positions_2robots
        if gridsize < 10:
            sample_start_positions = sample_start_positions_2robots_small

    # Run the model 50 times and render the output
    for s in range(num_start_positions):
        #print(str(_))
        # Reset the environment and set the starting positions
        obs = gym_env.reset()
        start_position = sample_start_positions[s]

        # Access the underlying environment and modify the robot positions
        gym_env.envs[0].robots = np.array(start_position, dtype=np.int32)

        # Get the observation again after setting the positions
        gym_env._save_obs(0, gym_env.envs[0]._get_observation())
        obs = gym_env._obs_from_buf()

        gym_env.render()
        if num_robots == 2:
            path_length = [0, 0]
        else:
            path_length = 0
        reward = 0

        if len(path_info) < 11:
            start_positions = [sample_start_positions[s][0]]
            path1 = {0: sample_start_positions[s][0]}
            path2 = {}
            if num_robots == 2:
                path2 = {0: sample_start_positions[s][1]}
                start_positions.append(sample_start_positions[s][1])

        # Max 50 steps
        for i in range(50):
            actions, _states = model.predict(obs, deterministic=False)
            obs, rewards, done, info = gym_env.step(actions)
            gym_env.render()
            #time.sleep(0.2)

            if num_robots == 2:
                for r in range(num_robots):
                    if not np.array_equal(obs['goals'][0][r], obs['robots'][0][r]):
                        path_length[r] += 1
            else:
                path_length += 1

            reward += rewards[0]

            if done:
                # print('DONE')
                number_successes += 1
                if num_robots == 2:
                    avg_path_length += (path_length[0] + path_length[1]) / 2
                    avg_EH += (info[0]['EH'][0] + info[0]['EH'][1]) / 2
                    path_EH = (info[0]['EH'][0] + info[0]['EH'][1]) / 2
                else:
                    avg_path_length += path_length
                    avg_EH += info[0]['EH'][0]
                    path_EH = info[0]['EH'][0]

                avg_reward += reward

                if len(path_info) < 11:
                    new_positions = obs['goals'][0]
                    path1[i + 1] = tuple(new_positions[0])
                    if num_robots == 2:
                        path2[i + 1] = tuple(new_positions[1])

                break

            if len(path_info) < 11:
                new_positions = obs['robots'][0]
                path1[i + 1] = tuple(new_positions[0])
                if num_robots == 2:
                    path2[i + 1] = tuple(new_positions[1])

        if not done:
            number_failures += 1

        if len(path_info) < 11:
            p_info = {'start_positions': start_positions, 'gridsize': gridsize, 'path1': path1, 'path2': path2}
            path_info.append(p_info)

    gym_env.close()

    avg_path_length /= num_start_positions
    avg_reward /= num_start_positions
    avg_reward /= 10
    avg_EH /= num_start_positions
    print("failures = " + str(number_failures))
    print("successes = " + str(number_successes))
    print("avg path length = " + str(avg_path_length))
    print("avg reward = " + str(avg_reward))
    print("avg EH = " + str(avg_EH))

    # Rounding the floating points to only have 2 decimals
    avg_reward = round(avg_reward, 2)
    avg_EH = round(avg_EH, 2)

    return number_failures, number_successes, avg_path_length, avg_reward, avg_EH, path_info
