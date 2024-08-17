from tests.util.test_env import *
from tests.util.models import *


def run_all_gridsize_tests():
    results_5 = {'standard1': test_gridsize_5_standard_1(),
                 'standard2': test_gridsize_5_standard_2()}

    results_20 = {'standard1': test_gridsize_20_standard_1(),
                  'standard2': test_gridsize_20_standard_2()}

    return {'gridsize5': results_5, 'gridsize20': results_20}


# Grid size = 5
def test_gridsize_5_standard_1():
    gridsize, goals, obstacles, lightsources = generate_small_model_1()
    gridsize = 5
    use_EH = False

    print('Test gridsize=5 standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    print('Test gridsize=5 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_gridsize_5_standard_2():
    gridsize, goals, obstacles, lightsources = generate_small_model_1()
    gridsize = 5
    use_EH = False

    print('Test gridsize=5 standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    print('Test gridsize=5 standard 2 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


# Grid size = 20
def test_gridsize_20_standard_1():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    gridsize = 20
    use_EH = False

    print('Test gridsize=20 standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    print('Test gridsize=20 standard 1 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_gridsize_20_standard_2():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    gridsize = 20
    use_EH = False

    print('Test gridsize=20 standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    print('Test gridsize=20 standard 2 EH')
    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}
