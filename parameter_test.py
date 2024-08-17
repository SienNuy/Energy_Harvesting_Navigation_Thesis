from tests.util.test_env import *
import csv

# To find the sweet spot for all kinds of parameters we will run a giant test

grid_size = 10
obstacles = [(3, 3), (5, 7), (8, 4)]

test_goals = [[(7, 2)],
              [(7, 2), (1, 1)]]


test_lightsources = [[(5, 5)],
                     [(2, 5), (5, 5), (8, 5)],
                     [(5, 5), (8, 5), (2, 5), (1, 2), (9, 2), (3, 9), (7, 9)],
                     [(5, 5), (4, 5), (6, 5), (5, 4), (5, 6), (4, 4), (6, 6)]]

training_timesteps1 = [20000, 50000]
training_timesteps2 = [50000, 100000]


def get_sample_start_positions():
    sample_start_pos_robot1 = []
    sample_start_pos_robot2 = []
    for i in range(50):
        while True:
            pos1 = (np.random.randint(grid_size), np.random.randint(grid_size))
            pos2 = (np.random.randint(grid_size), np.random.randint(grid_size))
            if pos1 != pos2:
                if (pos1 not in obstacles and pos1 not in sample_start_pos_robot1 and pos1 not in [(7, 2), (1, 1)] and
                        pos2 not in obstacles and pos2 not in sample_start_pos_robot2 and pos2 not in [(7, 2), (1, 1)]):
                    sample_start_pos_robot1.append(pos1)
                    sample_start_pos_robot2.append(pos2)
                    break

    print(sample_start_pos_robot1)
    print('\n')
    print(sample_start_pos_robot2)


sample_start_pos_robot1 = [(0, 2), (6, 7), (0, 7), (8, 3), (1, 2), (9, 7), (9, 8), (3, 7), (3, 1), (8, 5), (2, 6),
                           (4, 5), (6, 3), (0, 8), (5, 5), (5, 3), (9, 4), (3, 0), (2, 1), (0, 5), (5, 2), (5, 6),
                           (5, 0), (6, 4), (5, 9), (1, 8), (9, 2), (0, 3), (7, 3), (1, 3), (0, 0), (2, 5), (4, 2),
                           (5, 1), (7, 6), (9, 1), (2, 4), (7, 0), (6, 8), (8, 1), (8, 0), (0, 9), (9, 9), (5, 4),
                           (7, 7), (1, 0), (1, 9), (2, 3), (4, 9), (3, 6)]

sample_start_pos_robot2 = [(4, 0), (9, 9), (5, 0), (0, 3), (9, 6), (5, 9), (6, 9), (4, 9), (9, 0), (6, 2), (7, 5),
                           (7, 3), (3, 0), (1, 5), (4, 2), (7, 4), (2, 8), (0, 6), (8, 8), (0, 9), (7, 1), (1, 7),
                           (9, 3), (4, 7), (4, 1), (5, 5), (3, 5), (8, 2), (3, 8), (1, 6), (5, 8), (8, 3), (0, 8),
                           (5, 4), (9, 2), (1, 8), (7, 7), (2, 2), (2, 9), (0, 2), (9, 5), (8, 6), (7, 9), (5, 6),
                           (4, 6), (2, 0), (9, 4), (2, 4), (8, 7), (7, 0)]

sample_start_positions_1robot = []
sample_start_positions_2robots = []
for i in range(50):
    sample_start_positions_1robot.append([sample_start_pos_robot1[i]])
    sample_start_positions_2robots.append([sample_start_pos_robot1[i], sample_start_pos_robot2[i]])

test_reward_done = [100, 500, 1000, 2000]
test_penalty_invalid_move = [-1, -2, -5]
test_penalty_collision = [-2, -5, -10]
test_penalty_move = [-0.1, -0.2, -0.5]
test_reward_EH = [2, 5]
test_reward_EH_power = [1, 2]


def run_parameter_test():
    with open('example.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['gridsize', 'num_robots', 'num_obstacles', 'num_lightsources', 'EH', 'reward_done',
                         'penalty_invalid_move', 'penalty_collision', 'penalty_move', 'reward_EH', 'reward_EH_power',
                         'timesteps', 'number_failures', 'number_successes', 'avg_path_length', 'avg_reward', 'avg_EH'])

        # GOALS
        for goals in test_goals:
            if len(goals) == 1:
                sample_start_positions = sample_start_positions_1robot
                training_timesteps = training_timesteps1
            elif len(goals) == 2:
                sample_start_positions = sample_start_positions_2robots
                training_timesteps = training_timesteps2

            # LIGHTSOURCES
            for lightsources in test_lightsources:

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

                                        for timesteps in training_timesteps:
                                            print('\n\nTESTING ')
                                            print('Grid size: \t' + str(grid_size))
                                            print('Number of Robots: \t' + str(len(goals)))
                                            print('Goals: \t' + str(goals))
                                            print('Obstacles: \t' + str(obstacles))
                                            print('Lightsources: \t' + str(lightsources))
                                            print('EH: \tFalse')
                                            print('Reward done \t' + str(reward_done))
                                            print('Penalty invalid move \t' + str(penalty_invalid_move))
                                            print('Penalty collision \t' + str(penalty_collision))
                                            print('Penalty move \t' + str(penalty_move))
                                            print('Reward EH \t' + str(reward_EH))
                                            print('Reward EH power\t' + str(reward_EH_power))
                                            print('Timesteps: \t' + str(timesteps))
                                            print('-------------------------------------------------------------------')

                                            str_lightsources = str(len(lightsources))
                                            if lightsources == test_lightsources[-1]:
                                                str_lightsources += '_clustered'
                                            file_name = ((str(grid_size)) + 'x' + str(grid_size) + '_' + str(len(goals))
                                                         + '_robots_' + str(len(obstacles)) + '_obs_' +
                                                         str_lightsources + '_lights' + '_reward_done=' +
                                                         str(reward_param['reward_done']) + '_penalty_invalid_move=' +
                                                         str(reward_param['penalty_invalid_move']) + '_penalty_collision=' +
                                                         str(reward_param['penalty_collision']) + '_penalty_move=' +
                                                         str(reward_param['penalty_move']) + '_reward_EH=' +
                                                         str(reward_param['reward_EH']) + '_reward_EH_power=' +
                                                         str(reward_param['reward_EH_power']))

                                            results_no_EH = test_gym_env(grid_size, goals, obstacles, lightsources,
                                                                         False, reward_param, timesteps,
                                                                         sample_start_positions, file_name)
                                            print('----------------------------------------------------------------\n')

                                            writer.writerow([
                                                str(grid_size),
                                                str(len(goals)),
                                                str(len(obstacles)),
                                                str(str_lightsources),
                                                'False',
                                                str(reward_param['reward_done']),
                                                str(reward_param['penalty_invalid_move']),
                                                str(reward_param['penalty_collision']),
                                                str(reward_param['penalty_move']),
                                                str(reward_param['reward_EH']),
                                                str(reward_param['reward_EH_power']),
                                                str(timesteps),
                                                str(results_no_EH['number_failures']),
                                                str(results_no_EH['number_successes']),
                                                str(results_no_EH['avg_path_length']),
                                                str(results_no_EH['avg_reward']),
                                                str(results_no_EH['avg_EH'])
                                            ])

                                            print('\n\nTESTING ')
                                            print('Grid size: \t' + str(grid_size))
                                            print('Number of Robots: \t' + str(len(goals)))
                                            print('Goals: \t' + str(goals))
                                            print('Obstacles: \t' + str(obstacles))
                                            print('Lightsources: \t' + str(lightsources))
                                            print('EH: \tTrue')
                                            print('Reward done \t' + str(reward_done))
                                            print('Penalty invalid move \t' + str(penalty_invalid_move))
                                            print('Penalty collision \t' + str(penalty_collision))
                                            print('Penalty move \t' + str(penalty_move))
                                            print('Reward EH \t' + str(reward_EH))
                                            print('Reward EH power\t' + str(reward_EH_power))
                                            print('Timesteps: \t' + str(timesteps))
                                            print('-----------------------------------------------------------------')

                                            results_EH = test_gym_env(grid_size, goals, obstacles, lightsources, True,
                                                                      reward_param, timesteps, sample_start_positions, file_name)
                                            print('-----------------------------------------------------------------\n')

                                            writer.writerow([
                                                str(grid_size),
                                                str(len(goals)),
                                                str(len(obstacles)),
                                                str(str_lightsources),
                                                'True',
                                                str(reward_param['reward_done']),
                                                str(reward_param['penalty_invalid_move']),
                                                str(reward_param['penalty_collision']),
                                                str(reward_param['penalty_move']),
                                                str(reward_param['reward_EH']),
                                                str(reward_param['reward_EH_power']),
                                                str(timesteps),
                                                str(results_EH['number_failures']),
                                                str(results_EH['number_successes']),
                                                str(results_EH['avg_path_length']),
                                                str(results_EH['avg_reward']),
                                                str(results_EH['avg_EH'])
                                            ])


run_parameter_test()
