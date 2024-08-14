from tests.util.test_env import *


# Grid size = 20
def test_grid_size_20_standard_1():
    # Get parameters
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_1()
    gridsize = 20
    use_EH = False

    # Test both environments
    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)


def test_grid_size_20_standard_2():
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_2()
    gridsize = 20
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)


# Grid size = 40
def test_grid_size_40_standard_1():
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_1()
    gridsize = 40
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)


def test_grid_size_40_standard_2():
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_2()
    gridsize = 40
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)
