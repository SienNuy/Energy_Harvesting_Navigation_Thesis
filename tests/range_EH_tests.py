from tests.util.test_env import *
from tests.util.models import *

def test_range_EH_2_standard_1():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
    range_EH = 2
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_range_EH_2_standard_2():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_2()
    range_EH = 2
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_range_EH_4_standard_1():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
    range_EH = 4
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_range_EH_4_standard_2():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_2()
    range_EH = 4
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}




