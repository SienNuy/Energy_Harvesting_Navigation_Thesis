from tests.util.test_env import *
from tests.util.models import *
from param_test.param_results import *
from tests.util.train_env import generate_file_name


def run_all_multi_robot_tests():
    my_envs_1, results_1 = test_one_robot(reward_param=reward_param_standard_model_1, episodes=episodes_standard_model_1,
                               max_timesteps=max_timesteps_standard_model_1,
                               total_timesteps=training_timesteps_standard_model_1)
    my_envs_2, results_2 = test_two_robots(reward_param=reward_param_standard_model_2, episodes=episodes_standard_model_2,
                                max_timesteps=max_timesteps_standard_model_2,
                                total_timesteps=training_timesteps_standard_model_2)

    info = {'1 Robot': results_1, '2 Robots': results_2}
    envs = {'my_envs_1': my_envs_1, 'my_envs_2': my_envs_2}
    return envs, info


def test_one_robot(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    my_env_no_EH, results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps, return_env=True)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)
    use_EH = True

    my_env_EH, results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps, return_env=True)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    info = {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}
    my_envs = {
        'my_env_no_EH': my_env_no_EH,
        'my_env_EH': my_env_EH
    }
    return my_envs, info


def test_two_robots(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    my_env_no_EH, results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps, return_env=True)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)
    use_EH = True

    my_env_EH, results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps, return_env=True)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    info = {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH}
    my_envs = {
        'my_env_no_EH': my_env_no_EH,
        'my_env_EH': my_env_EH
    }
    return my_envs, info

