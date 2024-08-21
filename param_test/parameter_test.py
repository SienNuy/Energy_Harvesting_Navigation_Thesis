from tests.util.test_env import *
from param_results import reward_param_standard_model_1, reward_param_standard_model_2
import csv

# To find the sweet spot for all kinds of parameters we will run a giant test

# Basic case
grid_size = 10
obstacles = [(3, 3), (5, 7), (8, 4)]
#lightsources = [(5, 5)]
lightsources = [(2, 5), (5, 5), (8, 5)]
reward_weight = 0.5
range_EH = 3

# 1 robot and 2 robots
test_goals1 = [(7, 2)]
test_goals2 = [(7, 2), (1, 1)]

# timesteps parameter set
training_timesteps1 = [20000, 50000]
training_timesteps2 = [50000, 100000]

# reward parameters sets
test_reward_done1 = [100, 500]
test_reward_done2 = [1000]
test_penalty_invalid_move = [-1, -2, -5]
test_penalty_collision = [-2, -5, -10]
test_penalty_move = [-0.1, -0.2, -0.5]
test_reward_EH = [2, 5]
test_reward_EH_power = [1, 2]


def run_parameter_test_gym_env(test_goals, num_start_positions, csv_file_name):
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['reward_done', 'penalty_invalid_move', 'penalty_collision', 'penalty_move', 'reward_EH',
                         'reward_EH_power', 'timesteps', 'EH_False', 'EHF_number_failures', 'EHF_number_successes',
                         'EHF_avg_path_length', 'EHF_avg_reward', 'EHF_avg_EH', 'EH_True', 'EHT_number_failures',
                         'EHT_number_successes', 'EHT_avg_path_length', 'EHT_avg_reward', 'EHT_avg_EH'])

        goals = test_goals
        if len(goals) == 1:
            training_timesteps = training_timesteps1
            test_reward_done = test_reward_done1
        elif len(goals) == 2:
            training_timesteps = training_timesteps2
            test_reward_done = test_reward_done2

        # REWARD DONE
        for reward_done in test_reward_done:

            # PENALTY INVALID MOVE
            for penalty_invalid_move in test_penalty_invalid_move:

                # PENALTY COLLISION
                for penalty_collision in test_penalty_collision:

                    # PENALTY MOVE
                    for penalty_move in test_penalty_move:

                        # REWARD EH
                        for reward_EH in test_reward_EH:

                            # REWARD EH POWER
                            for reward_EH_power in test_reward_EH_power:

                                reward_param = {
                                    'reward_done': reward_done,
                                    'penalty_invalid_move': penalty_invalid_move,
                                    'penalty_collision': penalty_collision,
                                    'penalty_move': penalty_move,
                                    'reward_EH': reward_EH,
                                    'reward_EH_power': reward_EH_power,
                                }

                                # TIMESTEPS
                                for timesteps in training_timesteps:
                                    print('\n\nTESTING ')
                                    print('Grid size: \t' + str(grid_size))
                                    print('Number of Robots: \t' + str(len(goals)))
                                    print('Goals: \t' + str(goals))
                                    print('Obstacles: \t' + str(obstacles))
                                    print('Lightsources: \t' + str(lightsources))
                                    print('Reward done \t' + str(reward_done))
                                    print('Penalty invalid move \t' + str(penalty_invalid_move))
                                    print('Penalty collision \t' + str(penalty_collision))
                                    print('Penalty move \t' + str(penalty_move))
                                    print('Reward EH \t' + str(reward_EH))
                                    print('Reward EH power\t' + str(reward_EH_power))
                                    print('Timesteps: \t' + str(timesteps))
                                    print('-------------------------------------------------------------------')
                                    print('EH: \tFalse')

                                    prefix_file = ('models/' + str(len(goals)) + '_robots/' +
                                                   str(len(lightsources)) + '_lights/')
                                    file_name = prefix_file + (
                                            (str(grid_size)) + 'x' + str(grid_size) + '_' + str(len(goals))
                                            + '_robots_' + str(len(obstacles)) + '_obs_' +
                                            str(len(lightsources)) + '_lights' + '_reward_done=' +
                                            str(reward_param['reward_done']) + '_penalty_invalid_move=' +
                                            str(reward_param['penalty_invalid_move']) + '_penalty_collision=' +
                                            str(reward_param['penalty_collision']) + '_penalty_move=' +
                                            str(reward_param['penalty_move']) + '_reward_EH=' +
                                            str(reward_param['reward_EH']) + '_reward_EH_power=' +
                                            str(reward_param['reward_EH_power']))

                                    results_no_EH = test_gym_env(gridsize=grid_size, goals=goals, obstacles=obstacles,
                                                                 lightsources=lightsources, use_EH=False,
                                                                 reward_param=reward_param, reward_weight=reward_weight,
                                                                 range_EH=range_EH, timesteps=timesteps,
                                                                 file_name=file_name,
                                                                 num_start_positions=num_start_positions)
                                    print('-----------------------------------------------------------------')
                                    print('-----------------------------------------------------------------')
                                    print('EH: \tTrue')

                                    results_EH = test_gym_env(gridsize=grid_size, goals=goals, obstacles=obstacles,
                                                              lightsources=lightsources, use_EH=True,
                                                              reward_param=reward_param, reward_weight=reward_weight,
                                                              range_EH=range_EH, timesteps=timesteps,
                                                              file_name=file_name,
                                                              num_start_positions=num_start_positions)
                                    print('-----------------------------------------------------------------\n')

                                    writer.writerow([
                                        str(reward_param['reward_done']),
                                        str(reward_param['penalty_invalid_move']),
                                        str(reward_param['penalty_collision']),
                                        str(reward_param['penalty_move']),
                                        str(reward_param['reward_EH']),
                                        str(reward_param['reward_EH_power']),
                                        str(timesteps),
                                        'False',
                                        str(results_no_EH['number_failures']),
                                        str(results_no_EH['number_successes']),
                                        str(results_no_EH['avg_path_length']),
                                        str(results_no_EH['avg_reward']),
                                        str(results_no_EH['avg_EH']),
                                        'True',
                                        str(results_EH['number_failures']),
                                        str(results_EH['number_successes']),
                                        str(results_EH['avg_path_length']),
                                        str(results_EH['avg_reward']),
                                        str(results_EH['avg_EH'])
                                    ])


#run_parameter_test_gym_env(test_goals1, 10, 'param_test_1robot_10start_d.csv')
#run_parameter_test_gym_env(test_goals1, 20, 'param_test_1robot_20start_d.csv')
#run_parameter_test_gym_env(test_goals1, 50, 'param_test_1robot_50start_d.csv')
run_parameter_test_gym_env(test_goals2, 10, 'param_test_2robot_10start.csv')
#run_parameter_test_gym_env(test_goals2, 20, 'param_test_2robot_20start.csv')
#run_parameter_test_gym_env(test_goals2, 50, 'param_test_2robot_50start.csv')


test_num_episodes1 = [1000, 5000, 10000]
test_num_episodes2 = [5000, 10000, 15000]
test_max_timesteps = [100, 200]


def run_parameter_test_my_env(test_goals, num_start_positions, csv_file_name, reward_param):
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Episodes', 'Max Timesteps', 'EH_False', 'EHF_number_failures', 'EHF_number_successes',
                         'EHF_avg_path_length', 'EHF_avg_reward', 'EHF_avg_EH', 'EH_True', 'EHT_number_failures',
                         'EHT_number_successes', 'EHT_avg_path_length', 'EHT_avg_reward', 'EHT_avg_EH'])

        goals = test_goals
        if len(goals) == 1:
            test_num_episodes = test_num_episodes1
        elif len(goals) == 2:
            test_num_episodes = test_num_episodes2

        # EPISODES
        for num_episodes in test_num_episodes:

            # MAX TIMESTEPS
            for max_timesteps in test_max_timesteps:
                print('\n\nTESTING ')
                print('Grid size: \t' + str(grid_size))
                print('Number of Robots: \t' + str(len(goals)))
                print('Goals: \t' + str(goals))
                print('Obstacles: \t' + str(obstacles))
                print('Lightsources: \t' + str(lightsources))
                print('Episodes: \t' + str(num_episodes))
                print('Max Timesteps: \t' + str(max_timesteps))
                print('-----------------------------------------------------------------')
                print('EH: \tFalse')
                results_no_EH = test_my_env(gridsize=grid_size, goals=goals, obstacles=obstacles,
                                            lightsources=lightsources, use_EH=False, reward_param=reward_param,
                                            reward_weight=reward_weight, range_EH=range_EH, episodes=num_episodes,
                                            max_timesteps=max_timesteps, num_start_positions=num_start_positions)

                print('-----------------------------------------------------------------')
                print('-----------------------------------------------------------------')
                print('EH: \tTrue')

                results_EH = test_my_env(gridsize=grid_size, goals=goals, obstacles=obstacles,
                                            lightsources=lightsources, use_EH=True, reward_param=reward_param,
                                            reward_weight=reward_weight, range_EH=range_EH, episodes=num_episodes,
                                            max_timesteps=max_timesteps, num_start_positions=num_start_positions)
                print('-----------------------------------------------------------------')

                writer.writerow([
                    str(num_episodes),
                    str(max_timesteps),
                    'False',
                    str(results_no_EH['number_failures']),
                    str(results_no_EH['number_successes']),
                    str(results_no_EH['avg_path_length']),
                    str(results_no_EH['avg_reward']),
                    str(results_no_EH['avg_EH']),
                    'True',
                    str(results_EH['number_failures']),
                    str(results_EH['number_successes']),
                    str(results_EH['avg_path_length']),
                    str(results_EH['avg_reward']),
                    str(results_EH['avg_EH'])
                ])


#reward_param1 = reward_param_standard_model_1
#run_parameter_test_my_env(test_goals1, 10, 'my_env_param_test_1robot_10start.csv', reward_param1)
#run_parameter_test_my_env(test_goals1, 20, 'my_env_param_test_1robot_20start.csv', reward_param1)
#run_parameter_test_my_env(test_goals1, 50, 'my_env_param_test_1robot_50start.csv', reward_param1)


#reward_param2 = reward_param_standard_model_2
#run_parameter_test_my_env(test_goals2, 10, 'results/my_env_param_test_2robots_10start.csv', reward_param2)
#run_parameter_test_my_env(test_goals2, 20, 'results/my_env_param_test_2robots_20start.csv', reward_param2)
#run_parameter_test_my_env(test_goals2, 50, 'results/my_env_param_test_2robots_50start.csv', reward_param2)
