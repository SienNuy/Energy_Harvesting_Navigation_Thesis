from tests.util.test_env import *


def test_one_robot():
    gridsize, goals, obstacles, lightsources = generate_standard_model_1()
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 50000)


def test_two_robots():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 200000)


def test_three_robots():
    gridsize, goals, obstacles, lightsources = generate_standard_model_2()
    goals.append((6, 5))
    use_EH = False

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 400000)

    use_EH = True

    test_my_env(gridsize, goals, obstacles, lightsources, use_EH)
    test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, 400000)
