from tests.utils.test_env import *
from tests.utils.models import *
from param_test.param_results import *
from tests.utils.train_env import generate_file_name
from util import generate_ratio_results
import csv


def run_all_lightsource_tests():
    results_1 = {'standard_model_1': test_1_lightsource_standard_1(reward_param=reward_param_standard_model_1,
                                                                episodes=episodes_standard_model_1,
                                                                max_timesteps=max_timesteps_standard_model_1,
                                                                total_timesteps=total_timesteps_standard_model_1),
                 'standard_model_2': test_1_lightsource_standard_2(reward_param=reward_param_standard_model_2,
                                                                episodes=episodes_standard_model_2,
                                                                max_timesteps=max_timesteps_standard_model_2,
                                                                total_timesteps=total_timesteps_standard_model_2)}

    results_7 = {'standard_model_1': test_7_lightsources_sparse_standard_1(reward_param=reward_param_standard_model_1,
                                                                episodes=episodes_standard_model_1,
                                                                max_timesteps=max_timesteps_standard_model_1,
                                                                total_timesteps=total_timesteps_standard_model_1),
                 'standard_model_2': test_7_lightsources_sparse_standard_2(reward_param=reward_param_standard_model_2,
                                                                episodes=episodes_standard_model_2,
                                                                max_timesteps=max_timesteps_standard_model_2,
                                                                total_timesteps=total_timesteps_standard_model_2)}

    results_7clustered = {'standard_model_1': test_7_lightsources_clustered_standard_1(reward_param=reward_param_standard_model_1,
                                                                episodes=episodes_standard_model_1,
                                                                max_timesteps=max_timesteps_standard_model_1,
                                                                total_timesteps=total_timesteps_standard_model_1),
                          'standard_model_2': test_7_lightsources_clustered_standard_2(reward_param=reward_param_standard_model_2,
                                                                episodes=episodes_standard_model_2,
                                                                max_timesteps=max_timesteps_standard_model_2,
                                                                total_timesteps=total_timesteps_standard_model_2)}

    return {'1 lightsource': results_1, '7 lightsources (sparse)': results_7,
            '7 lightsources (clustered)': results_7clustered}


def test_1_lightsource_standard_1(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
    lightsources = [(5, 5)]
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    print('Test 1 lightsource standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test 1 lightsource standard 1 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


def test_1_lightsource_standard_2(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
    lightsources = [(5, 5)]
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    print('Test 1 lightsource standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test 1 lightsource standard 2 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


def test_7_lightsources_sparse_standard_1(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
    lightsources += [(1, 2), (9, 2), (3, 9), (7, 9)]
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    print('Test 7 lightsources standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test 7 lightsources standard 1 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


def test_7_lightsources_sparse_standard_2(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
    lightsources += [(1, 2), (9, 2), (3, 9), (7, 9)]
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources)
    use_EH = False

    print('Test 7 lightsources standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test 7 lightsources standard 2 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


def test_7_lightsources_clustered_standard_1(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
    lightsources = [(5, 5), (4, 5), (6, 5), (5, 4), (5, 6), (4, 4), (6, 6)]
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources, clustered=True)
    use_EH = False

    print('Test 7 lightsources clustered standard 1 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test 7 lightsources clustered standard 1  EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


def test_7_lightsources_clustered_standard_2(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
    lightsources = [(5, 5), (4, 5), (6, 5), (5, 4), (5, 6), (4, 4), (6, 6)]
    file_name = generate_file_name(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources, clustered=True)
    use_EH = False

    print('Test 7 lightsources clustered standard 2 No EH')
    results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                   use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                   range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                     use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                     range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    use_EH = True

    print('Test 7 lightsources clustered standard 2 EH')
    results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

    results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


##################################################################################################################

def run_parameter_lightsource_tests():
    test_reward_EH_power = [1, 2]

    test_reward_EH_light1 = [2, 3]
    lightsources = [(5, 5)]
    lightsource_str = str(len(lightsources))
    # Standard model 1 - 1 Light
    run_parameter_lightsource_test_gym_env(1, lightsources, test_reward_EH_light1, test_reward_EH_power, lightsource_str)
    # Standard model 2 - 1 Light
    run_parameter_lightsource_test_gym_env(2, lightsources, test_reward_EH_light1, test_reward_EH_power, lightsource_str)

    test_reward_EH_light7 = [2, 5, 10]
    lightsources = [(2, 5), (5, 5), (8, 5), (1, 2), (9, 2), (3, 9), (7, 9)]
    lightsource_str = str(len(lightsources))
    # Standard model 1 - 7 Lights
    run_parameter_lightsource_test_gym_env(1, lightsources, test_reward_EH_light7, test_reward_EH_power, lightsource_str)
    # Standard model 2 - 7 Lights
    run_parameter_lightsource_test_gym_env(2, lightsources, test_reward_EH_light7, test_reward_EH_power, lightsource_str)

    test_reward_EH_light7_clustered = [2, 5, 10]
    lightsources = [(5, 5), (4, 5), (6, 5), (5, 4), (5, 6), (4, 4), (6, 6)]
    lightsource_str = str(len(lightsources)) + '_clustered'
    # Standard model 1 - 7 Lights clustered
    run_parameter_lightsource_test_gym_env(1, lightsources, test_reward_EH_light7_clustered, test_reward_EH_power, lightsource_str)
    # Standard model 2 - 7 Lights clustered
    run_parameter_lightsource_test_gym_env(2, lightsources, test_reward_EH_light7_clustered, test_reward_EH_power, lightsource_str)


def run_parameter_lightsource_test_gym_env(model, lightsources, test_reward_EH, test_reward_EH_power, lightsource_str):
    if model == 1:
        csv_file = "param_test_model1_lights=" + lightsource_str + '_gym_env.csv'
        gridsize, goals, obstacles, lights, reward_weight, range_EH = generate_standard_model_1()
        reward_param = reward_param_standard_model_1
        total_timesteps = total_timesteps_standard_model_1
    elif model == 2:
        csv_file = "param_test_model2_lights=" + lightsource_str + '_gym_env.csv'
        gridsize, goals, obstacles, lights, reward_weight, range_EH = generate_standard_model_2()
        reward_param = reward_param_standard_model_2
        total_timesteps = total_timesteps_standard_model_2
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['reward_EH', 'reward_EH_power', 'EH_False', 'EHF_number_failures', 'EHF_number_successes',
                         'EHF_avg_path_length', 'EHF_avg_reward', 'EHF_avg_EH', 'EH_True', 'EHT_number_failures',
                         'EHT_number_successes', 'EHT_avg_path_length', 'EHT_avg_reward', 'EHT_avg_EH'])

        for reward_EH in test_reward_EH:
            for reward_EH_power in test_reward_EH_power:
                reward_param['reward_EH'] = reward_EH
                reward_param['reward_EH_power'] = reward_EH_power

                file_name = "model_" + str(model) + "_lights=" + lightsource_str + "_rEH=" + str(reward_EH) + "_rEHp=" + str(reward_EH_power)
                results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles,
                                                 lightsources=lightsources,
                                                 use_EH=False, reward_param=reward_param, reward_weight=reward_weight,
                                                 range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)
                results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles,
                                              lightsources=lightsources,
                                              use_EH=True, reward_param=reward_param, reward_weight=reward_weight,
                                              range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

            writer.writerow([
                str(reward_EH),
                str(reward_EH_power),
                'False',
                str(results_gym_no_EH['number_failures']),
                str(results_gym_no_EH['number_successes']),
                str(results_gym_no_EH['avg_path_length']),
                str(results_gym_no_EH['avg_reward']),
                str(results_gym_no_EH['avg_EH']),
                'True',
                str(results_gym_EH['number_failures']),
                str(results_gym_EH['number_successes']),
                str(results_gym_EH['avg_path_length']),
                str(results_gym_EH['avg_reward']),
                str(results_gym_EH['avg_EH'])
            ])
