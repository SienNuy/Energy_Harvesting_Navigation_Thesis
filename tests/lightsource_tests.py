from tests.util.test_env import *


def test_1_lightsource_standard_1():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    lightsources = (5, 5)
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)


def test_1_lightsource_standard_2():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    lightsources = (5, 5)
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)


def test_7_lightsources_sparse_standard_1():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    lightsources += [(1, 2), (9, 2), (3, 9), (7, 9)]
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)


def test_7_lightsources_sparse_standard_2():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    lightsources += [(1, 2), (9, 2), (3, 9), (7, 9)]
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)


def test_7_lightsources_clustered_standard_1():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    lightsources = [(5, 5), (4, 5), (6, 5), (5, 4), (5, 6), (4, 4), (6, 6)]
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)


def test_7_lightsources_clustered_standard_2():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    lightsources = [(5, 5), (4, 5), (6, 5), (5, 4), (5, 6), (4, 4), (6, 6)]
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)
