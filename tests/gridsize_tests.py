from tests.util.test_env import *
from tests.util.models import *
from param_test.param_results import *
from tests.util.train_env import generate_file_name


def run_all_gridsize_tests():
    results_5 = {'standard_model_1': test_gridsize_5_standard_1(reward_param=reward_param_standard_model_1,
                                                                episodes=episodes_standard_model_1,
                                                                max_timesteps=max_timesteps_standard_model_1,
                                                                total_timesteps=training_timesteps_standard_model_1),
                 'standard_model_2': test_gridsize_5_standard_2(reward_param=reward_param_standard_model_2,
                                                                episodes=episodes_standard_model_2,
                                                                max_timesteps=max_timesteps_standard_model_2,
                                                                total_timesteps=training_timesteps_standard_model_2)}

    results_20 = {'standard_model_1': test_gridsize_20_standard_1(reward_param=reward_param_standard_model_1,
                                                                  episodes=episodes_standard_model_1,
                                                                  max_timesteps=max_timesteps_standard_model_1,
                                                                  total_timesteps=training_timesteps_standard_model_1),
                  'standard_model_2': test_gridsize_20_standard_2(reward_param=reward_param_standard_model_2,
                                                                  episodes=episodes_standard_model_2,
                                                                  max_timesteps=max_timesteps_standard_model_2,
                                                                  total_timesteps=training_timesteps_standard_model_2)}

    return {'5x5': results_5, '20x20': results_20}


# Grid size = 5
def test_gridsize_5_standard_1(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
    gridsize = 5
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    print('Test gridsize=5 standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test gridsize=5 standard 1 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_gridsize_5_standard_2(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
    gridsize = 5
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    print('Test gridsize=5 standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test gridsize=5 standard 2 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


# Grid size = 20
def test_gridsize_20_standard_1(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
    gridsize = 20
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    print('Test gridsize=20 standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test gridsize=20 standard 1 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}


def test_gridsize_20_standard_2(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
    gridsize = 20
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    print('Test gridsize=20 standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test gridsize=20 standard 2 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}
