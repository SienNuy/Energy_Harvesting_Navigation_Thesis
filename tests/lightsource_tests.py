from tests.util.test_env import *
from tests.util.models import *


def run_all_gridsize_tests():
    results_1 = {'Standard Model 1': test_1_lightsource_standard_1(),
                 'Standard Model 2': test_1_lightsource_standard_2()}

    results_7 = {'Standard Model 1': test_7_lightsources_sparse_standard_1(),
                 'Standard Model 2': test_7_lightsources_sparse_standard_2()}

    results_7clustered = {'Standard Model 1': test_7_lightsources_clustered_standard_1(),
                          'Standard Model 2': test_7_lightsources_clustered_standard_2()}

    return {'1 lightsource': results_1, '7 lightsources (sparse)': results_7,
            '7 lightsources (clustered)': results_7clustered}


def test_1_lightsource_standard_1():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    lightsources = (5, 5)
    use_EH = False

    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}

def test_1_lightsource_standard_2():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    lightsources = (5, 5)
    use_EH = False

    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_7_lightsources_sparse_standard_1():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    lightsources += [(1, 2), (9, 2), (3, 9), (7, 9)]
    use_EH = False

    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_7_lightsources_sparse_standard_2():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    lightsources += [(1, 2), (9, 2), (3, 9), (7, 9)]
    use_EH = False

    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_7_lightsources_clustered_standard_1():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    lightsources = [(5, 5), (4, 5), (6, 5), (5, 4), (5, 6), (4, 4), (6, 6)]
    use_EH = False

    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_7_lightsources_clustered_standard_2():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    lightsources = [(5, 5), (4, 5), (6, 5), (5, 4), (5, 6), (4, 4), (6, 6)]
    use_EH = False

    results_my_no_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_no_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    results_my_EH = test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    results_gym_EH = test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}
