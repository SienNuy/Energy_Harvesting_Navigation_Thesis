import time
import numpy as np
from stable_baselines3.common.vec_env.util import dict_to_obs
from util import sample_start_positions_1robot, sample_start_positions_2robots


def navigate_my_env(my_env, num_start_positions):
    number_failures = 0
    number_successes = 0

    avg_path_length = 0
    avg_EH = 0
    avg_reward = 0

    if len(my_env.robots) == 1:
        sample_start_positions = sample_start_positions_1robot

    elif len(my_env.robots) == 2:
        sample_start_positions = sample_start_positions_2robots

    # Run the model 50 times
    for s in range(num_start_positions):
        my_env.reset()
        start_position = sample_start_positions[s]
        for r in range(len(my_env.robots)):
            my_env.robots[r].reset(start_position[r])

        path = {}
        for robot in my_env.robots:
            path[robot.id] = []

        path_length_ = 0
        reward_ = 0
        EH_ = 0

        # Max 50 steps
        for i in range(50):
            for robot in my_env.robots:
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

                # Check if we're going in circles > chose next best action
                # elif next_state in path[robot.id]:
                #     print('ERROR We has a situation where we would go back to a previous state')
                #     # go on with second best action
                #     # reset robot to the current state
                #     robot.position = state
                #     # Get the indices that would sort the array
                #     sorted_indices = np.argsort(q_values)
                #     # get second_best_action
                #     second_best_action = sorted_indices[-2]
                #     next_state, reward = my_env.step(robot, second_best_action)

                path[robot.id].append(next_state)
                reward_ += reward
                path_length_ += 1
                EH_ += robot.harvested_energy

            if my_env.done():
                number_successes += 1

                avg_path_length += path_length_
                avg_EH += EH_
                avg_reward += reward_
                break

        if not my_env.done():
            number_failures += 1

    avg_path_length /= num_start_positions
    avg_reward /= num_start_positions
    avg_EH /= num_start_positions
    print("failures = " + str(number_failures))
    print("successes = " + str(number_successes))
    print("avg path length = " + str(avg_path_length))
    print("avg reward = " + str(avg_reward))
    print("avg EH = " + str(avg_EH))

    return number_failures, number_successes, avg_path_length, avg_reward, avg_EH


def navigate_gym_env(gym_env, model, num_robots, num_start_positions):
    number_failures = 0
    number_successes = 0

    avg_path_length = 0
    avg_EH = 0
    avg_reward = 0

    if num_robots == 1:
        sample_start_positions = sample_start_positions_1robot

    elif num_robots == 2:
        sample_start_positions = sample_start_positions_2robots

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

        #gym_env.render()

        path_length = 0
        reward = 0
        EH = 0

        # Max 50 steps
        for i in range(50):
            actions, _states = model.predict(obs, deterministic=False)
            obs, rewards, done, info = gym_env.step(actions)
            #gym_env.render()
            #time.sleep(0.2)

            path_length += 1
            reward += rewards[0]
            for r in range(num_robots):
                EH += info[0]['EH'][r]
            if done:
                # print('DONE')
                number_successes += 1

                avg_path_length += path_length
                avg_EH += EH
                avg_reward += reward

                break
        if not done:
            number_failures += 1

    gym_env.close()

    avg_path_length /= num_start_positions
    avg_reward /= num_start_positions
    avg_EH /= num_start_positions
    print("failures = " + str(number_failures))
    print("successes = " + str(number_successes))
    print("avg path length = " + str(avg_path_length))
    print("avg reward = " + str(avg_reward))
    print("avg EH = " + str(avg_EH))

    return number_failures, number_successes, avg_path_length, avg_reward, avg_EH
