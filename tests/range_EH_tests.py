from tests.util.test_env import *
from tests.util.models import *
from param_test.param_results import *
from tests.util.train_env import generate_file_name


def run_all_range_EH_tests():
    results_2 = {'standard_model_1': test_range2_standard_1(reward_param=reward_param_standard_model_1,
                                                             episodes=episodes_standard_model_1,
                                                             max_timesteps=max_timesteps_standard_model_1,
                                                             total_timesteps=training_timesteps_standard_model_1),
                 'standard_model_2': test_range2_standard_2(reward_param=reward_param_standard_model_2,
                                                             episodes=episodes_standard_model_2,
                                                             max_timesteps=max_timesteps_standard_model_2,
                                                             total_timesteps=training_timesteps_standard_model_2)}

    results_5 = {'standard_model_1': test_range5_standard_1(reward_param=reward_param_standard_model_1,
                                                             episodes=episodes_standard_model_1,
                                                             max_timesteps=max_timesteps_standard_model_1,
                                                             total_timesteps=training_timesteps_standard_model_1),
                 'standard_model_2': test_range5_standard_2(reward_param=reward_param_standard_model_2,
                                                             episodes=episodes_standard_model_2,
                                                             max_timesteps=max_timesteps_standard_model_2,
                                                             total_timesteps=training_timesteps_standard_model_2)}


    return {'Range EH = 2': results_2, 'Range EH = 5': results_5}


def test_range2_standard_1(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
    range_EH = 2
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   range_EH=range_EH)
    use_EH = False

    print('Test range=2 standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test range=2 standard 1 EH')
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


def test_range2_standard_2(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
    range_EH = 2
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   range_EH=range_EH)
    use_EH = False

    print('Test range=2 standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test range=2 standard 2 EH')
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


def test_range5_standard_1(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
    range_EH = 5
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   range_EH=range_EH)
    use_EH = False

    print('Test range=5 standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test range=5 standard 1 EH')
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


def test_range5_standard_2(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
    range_EH = 5
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   range_EH=range_EH)

    use_EH = False

    print('Test range=5 standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test range=5 standard 2 EH')
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

