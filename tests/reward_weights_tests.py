from tests.util.test_env import *
from tests.util.models import *


def run_all_reward_weights_tests():
    results_4 = {'Standard Model 1': test_reward_weights_4_standard_1(),
                 'Standard Model 2': test_reward_weights_4_standard_2()}

    results_6 = {'Standard Model 1': test_reward_weights_6_standard_1(),
                 'Standard Model 2': test_reward_weights_6_standard_2()}

    results_8 = {'Standard Model 1': test_reward_weights_8_standard_1(),
                 'Standard Model 2': test_reward_weights_8_standard_2()}

    return {'Reward Weight = 0.4': results_4, 'Reward Weight = 0.6': results_6, 'Reward Weight = 0.8': results_8}


def test_reward_weights_4_standard_1():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
    reward_weight = 0.4
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_reward_weights_4_standard_2():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_2()
    reward_weight = 0.4
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_reward_weights_6_standard_1():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
    reward_weight = 0.6
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_reward_weights_6_standard_2():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_2()
    reward_weight = 0.6
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_reward_weights_8_standard_1():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
    reward_weight = 0.8
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_reward_weights_8_standard_2():
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_2()
    reward_weight = 0.8
    use_EH = True

    print('Test reward_weight=0.4 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}
