import time
import numpy as np


def navigate_my_env(my_env):
    number_failures = 0
    number_successes = 0

    avg_path_length = 0
    avg_EH = 0
    avg_reward = 0

    # Run the model 50 times
    for _ in range(50):
        my_env.reset()

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
                next_state, reward = my_env.step(robot, best_action)

                # Check if there is a collision > choose next best action
                if next_state == state:
                    if reward == -15:  # collision so choose next best action
                        # go on with second best action
                        # Get the indices that would sort the array
                        sorted_indices = np.argsort(q_values)
                        # get second_best_action
                        second_best_action = sorted_indices[-2]
                        next_state, reward = my_env.step(robot, second_best_action)
                        print('COLLISION AVOIDANCE')
                    else:
                        print('ERROR something went wrong finding the path')

                # Check if we're going in circles > chose next best action
                elif next_state in path[robot.id]:
                    print('ERROR We has a situation where we would go back to a previous state')
                    # go on with second best action
                    # reset robot to the current state
                    robot.position = state
                    # Get the indices that would sort the array
                    sorted_indices = np.argsort(q_values)
                    # get second_best_action
                    second_best_action = sorted_indices[-2]
                    next_state, reward = my_env.step(robot, second_best_action)

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

    avg_path_length /= 50
    avg_reward /= 50
    avg_EH /= 50
    print("failures = " + str(number_failures))
    print("successes = " + str(number_successes))
    print("avg path length = " + str(avg_path_length))
    print("avg reward = " + str(avg_reward))
    print("avg EH = " + str(avg_EH))

    return number_failures, number_successes, avg_path_length, avg_reward, avg_EH


def navigate_gym_env(gym_env, model):
    number_failures = 0
    number_successes = 0

    avg_path_length = 0
    avg_EH = 0
    avg_reward = 0

    # Run the model 50 times and render the output
    for _ in range(50):
        obs = gym_env.reset()
        gym_env.render()

        path_length = 0
        reward = 0
        EH = 0

        # Max 50 steps
        for i in range(50):
            print(str(i))
            actions, _states = model.predict(obs, deterministic=False)
            obs, rewards, done, info = gym_env.step(actions)
            gym_env.render()
            time.sleep(0.5)

            path_length += 1
            reward += rewards[0]
            EH += info[0]['EH'][0]
            if done:
                print('DONE')
                number_successes += 1

                avg_path_length += path_length
                avg_EH += EH
                avg_reward += reward

                break
        if not done:
            number_failures += 1

    gym_env.close()

    avg_path_length /= 50
    avg_reward /= 50
    avg_EH /= 50
    print("failures = " + str(number_failures))
    print("successes = " + str(number_successes))
    print("avg path length = " + str(avg_path_length))
    print("avg reward = " + str(avg_reward))
    print("avg EH = " + str(avg_EH))

    return number_failures, number_successes, avg_path_length, avg_reward, avg_EH
