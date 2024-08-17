from tests.util.test_env import *
from tests.util.models import *


def run_all_multi_robot_tests():
    results_1 = test_one_robot()
    results_2 = test_two_robots()
    results_3 = test_three_robots()

    return {'1robot': results_1, '2robots': results_2, '3robots': results_3}


def test_one_robot():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    use_EH = False

    #results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    #results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': None,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': None,
            'results_gym_EH': results_gym_EH}


def test_two_robots():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    use_EH = False

    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_three_robots():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    goals.append((6, 5))
    use_EH = False

    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 400000)

    use_EH = True

    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 400000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}
