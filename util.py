import numpy as np
from tests.utils.models import *


def get_sample_start_positions(grid_size, obstacles, goals):
    sample_start_pos_robot1 = []
    sample_start_pos_robot2 = []
    for i in range(10):
        while True:
            pos1 = (np.random.randint(grid_size), np.random.randint(grid_size))
            pos2 = (np.random.randint(grid_size), np.random.randint(grid_size))
            if pos1 != pos2:
                if (pos1 not in obstacles and pos1 not in sample_start_pos_robot1 and pos1 not in goals and
                        pos2 not in obstacles and pos2 not in sample_start_pos_robot2 and pos2 not in goals):
                    sample_start_pos_robot1.append(pos1)
                    sample_start_pos_robot2.append(pos2)
                    break

    print(sample_start_pos_robot1)
    print('\n')
    print(sample_start_pos_robot2)


temp_sample_start_pos_robot1 = [(0, 2), (6, 7), (0, 7), (8, 3), (1, 2), (9, 7), (9, 8), (3, 7), (3, 1), (8, 5), (2, 6),
                                (4, 5), (6, 3), (0, 8), (5, 5), (5, 3), (9, 4), (3, 0), (2, 1), (0, 5), (5, 2), (5, 6),
                                (5, 0), (6, 4), (5, 9), (1, 8), (9, 2), (0, 3), (7, 3), (1, 3), (0, 0), (2, 5), (4, 2),
                                (5, 1), (7, 6), (9, 1), (2, 4), (7, 0), (6, 8), (8, 1), (8, 0), (0, 9), (9, 9), (5, 4),
                                (7, 7), (1, 0), (1, 9), (2, 3), (4, 9), (3, 6)]

temp_sample_start_pos_robot2 = [(4, 0), (9, 9), (5, 0), (0, 3), (9, 6), (5, 9), (6, 9), (4, 9), (9, 0), (6, 2), (7, 5),
                                (7, 3), (3, 0), (1, 5), (4, 2), (7, 4), (2, 8), (0, 6), (8, 8), (0, 9), (7, 1), (1, 7),
                                (9, 3), (4, 7), (4, 1), (5, 5), (3, 5), (8, 2), (3, 8), (1, 6), (5, 8), (8, 3), (0, 8),
                                (5, 4), (9, 2), (1, 8), (7, 7), (2, 2), (2, 9), (0, 2), (9, 5), (8, 6), (7, 9), (5, 6),
                                (4, 6), (2, 0), (9, 4), (2, 4), (8, 7), (7, 0)]


def get_sample_start_positions_1robot(temp_sample_start_pos_robot1):
    sample_start_positions_1robot = []
    for i in range(len(temp_sample_start_pos_robot1)):
        sample_start_positions_1robot.append([temp_sample_start_pos_robot1[i]])

    print(sample_start_positions_1robot)


def get_sample_start_positions_2robots(temp_sample_start_pos_robot1, temp_sample_start_pos_robot2):
    sample_start_positions_2robots = []
    for i in range(len(temp_sample_start_pos_robot1)):
        sample_start_positions_2robots.append([temp_sample_start_pos_robot1[i], temp_sample_start_pos_robot2[i]])

    print(sample_start_positions_2robots)


# sample_start_positions_1robot = get_sample_start_positions_1robot()
# sample_start_positions_2robots = get_sample_start_positions_2robots()

sample_start_positions_1robot = [[(0, 2)], [(6, 7)], [(0, 7)], [(8, 3)], [(1, 2)], [(9, 7)], [(9, 8)], [(3, 7)],
                                 [(3, 1)], [(8, 5)], [(2, 6)], [(4, 5)], [(6, 3)], [(0, 8)], [(5, 5)], [(5, 3)],
                                 [(9, 4)], [(3, 0)], [(2, 1)], [(0, 5)], [(5, 2)], [(5, 6)], [(5, 0)], [(6, 4)],
                                 [(5, 9)], [(1, 8)], [(9, 2)], [(0, 3)], [(7, 3)], [(1, 3)], [(0, 0)], [(2, 5)],
                                 [(4, 2)], [(5, 1)], [(7, 6)], [(9, 1)], [(2, 4)], [(7, 0)], [(6, 8)], [(8, 1)],
                                 [(8, 0)], [(0, 9)], [(9, 9)], [(5, 4)], [(7, 7)], [(1, 0)], [(1, 9)], [(2, 3)],
                                 [(4, 9)], [(3, 6)]]

sample_start_positions_2robots = [[(0, 2), (4, 0)], [(6, 7), (9, 9)], [(0, 7), (5, 0)], [(8, 3), (0, 3)],
                                  [(1, 2), (9, 6)], [(9, 7), (5, 9)], [(9, 8), (6, 9)], [(3, 7), (4, 9)],
                                  [(3, 1), (9, 0)], [(8, 5), (6, 2)], [(2, 6), (7, 5)], [(4, 5), (7, 3)],
                                  [(6, 3), (3, 0)], [(0, 8), (1, 5)], [(5, 5), (4, 2)], [(5, 3), (7, 4)],
                                  [(9, 4), (2, 8)], [(3, 0), (0, 6)], [(2, 1), (8, 8)], [(0, 5), (0, 9)],
                                  [(5, 2), (7, 1)], [(5, 6), (1, 7)], [(5, 0), (9, 3)], [(6, 4), (4, 7)],
                                  [(5, 9), (4, 1)], [(1, 8), (5, 5)], [(9, 2), (3, 5)], [(0, 3), (8, 2)],
                                  [(7, 3), (3, 8)], [(1, 3), (1, 6)], [(0, 0), (5, 8)], [(2, 5), (8, 3)],
                                  [(4, 2), (0, 8)], [(5, 1), (5, 4)], [(7, 6), (9, 2)], [(9, 1), (1, 8)],
                                  [(2, 4), (7, 7)], [(7, 0), (2, 2)], [(6, 8), (2, 9)], [(8, 1), (0, 2)],
                                  [(8, 0), (9, 5)], [(0, 9), (8, 6)], [(9, 9), (7, 9)], [(5, 4), (5, 6)],
                                  [(7, 7), (4, 6)], [(1, 0), (2, 0)], [(1, 9), (9, 4)], [(2, 3), (2, 4)],
                                  [(4, 9), (8, 7)], [(3, 6), (7, 0)]]

#################
print('start')

temp_sample_start_pos_robot1_small = [(2, 2), (4, 0), (4, 3), (1, 4), (0, 0), (4, 4), (0, 2), (2, 1), (3, 2), (2, 3)]
temp_sample_start_pos_robot2_small = [(1, 3), (1, 0), (0, 3), (4, 4), (4, 1), (3, 0), (0, 1), (1, 4), (2, 1), (4, 0)]

#get_sample_start_positions_1robot(temp_sample_start_pos_robot1_small)
#get_sample_start_positions_2robots(temp_sample_start_pos_robot1_small, temp_sample_start_pos_robot2_small)

sample_start_positions_1robot_small = [[(2, 2)], [(4, 0)], [(4, 3)], [(1, 4)], [(0, 0)], [(4, 4)], [(0, 2)], [(2, 1)],
                                       [(3, 2)], [(2, 3)]]

sample_start_positions_2robots_small = [[(2, 2), (1, 3)], [(4, 0), (1, 0)], [(4, 3), (0, 3)], [(1, 4), (4, 4)],
                                        [(0, 0), (4, 1)], [(4, 4), (3, 0)], [(0, 2), (0, 1)], [(2, 1), (1, 4)],
                                        [(3, 2), (2, 1)], [(2, 3), (4, 0)]]


def generate_ratio_results(results_no_EH, results_EH):
    anomaly = False
    if results_EH["avg_EH"] <= results_no_EH["avg_EH"]:
        anomaly = True
    EH_ratio = results_EH["avg_EH"] / results_no_EH["avg_EH"] * 100
    path_ratio = results_EH["avg_path_length"] / results_no_EH["avg_path_length"] * 100

    trade_off = EH_ratio/path_ratio * 100

    # Rounding the floating points to only have 2 decimals
    EH_ratio = round(EH_ratio, 2)
    path_ratio = round(path_ratio, 2)
    trade_off = round(trade_off, 2)

    return {'Anomaly': anomaly,
            'EH_ratio': EH_ratio,
            'Path_ratio': path_ratio,
            'Trade_off': trade_off}
