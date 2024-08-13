from test_env import *


def test_grid_size_10_standard_1():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    gridsize = 10
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)


def test_grid_size_10_standard_2():
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_2()
    gridsize = 10
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)


# Grid size = 20
def test_grid_size_20_standard_1():
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_1()
    gridsize = 20

    # Test my environment
    my_env = build_my_environment(gridsize, goals, obstacles, lightsources, use_EH)

    # Test gym environment
    gym_env = build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH)


def test_grid_size_20_standard_2():
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_2()
    gridsize = 20

    # Test my environment
    my_env = build_my_environment(gridsize, goals, obstacles, lightsources, use_EH)

    # Test gym environment
    gym_env = build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH)


# Grid size = 40
def test_grid_size_40_standard_1():
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_1()
    gridsize = 40

    # Test my environment
    my_env = build_my_environment(gridsize, goals, obstacles, lightsources, use_EH)

    # Test gym environment
    gym_env = build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH)


def test_grid_size_40_standard_2():
    gridsize, goals, obstacles, lightsources, use_EH = generate_standard_model_2()
    gridsize = 40

    # Test my environment
    my_env = build_my_environment(gridsize, goals, obstacles, lightsources, use_EH)

    # Test gym environment
    gym_env = build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH)
