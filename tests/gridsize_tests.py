from tests.utils.test_env import *
from tests.utils.models import *
from param_test.param_results import *
from tests.utils.train_env import generate_file_name
from util import generate_ratio_results
import csv


def run_all_gridsize_tests():
    results_5 = {'standard_model_1': test_gridsize_5_standard_1(reward_param=reward_param_standard_model_1,
                                                                episodes=episodes_standard_model_1,
                                                                max_timesteps=max_timesteps_standard_model_1,
                                                                total_timesteps=total_timesteps_standard_model_1),
                 'standard_model_2': test_gridsize_5_standard_2(reward_param=reward_param_standard_model_2,
                                                                episodes=episodes_standard_model_2,
                                                                max_timesteps=max_timesteps_standard_model_2,
                                                                total_timesteps=total_timesteps_standard_model_2)}

    results_20 = {'standard_model_1': test_gridsize_20_standard_1(reward_param=reward_param_standard_model_1,
                                                                  episodes=episodes_standard_model_1,
                                                                  max_timesteps=max_timesteps_standard_model_1,
                                                                  total_timesteps=total_timesteps_standard_model_1),
                  'standard_model_2': test_gridsize_20_standard_2(reward_param=reward_param_standard_model_2,
                                                                  episodes=episodes_standard_model_2,
                                                                  max_timesteps=max_timesteps_standard_model_2,
                                                                  total_timesteps=total_timesteps_standard_model_2)}

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

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


def test_gridsize_5_standard_2(reward_param, episodes, max_timesteps, total_timesteps):
    gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_2()
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

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


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

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


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

    ratio_results_my = generate_ratio_results(results_no_EH=results_my_no_EH, results_EH=results_my_EH)
    ratio_results_gym = generate_ratio_results(results_no_EH=results_gym_no_EH, results_EH=results_gym_EH)
    return {'results_my_no_EH': results_my_no_EH,
            'results_gym_no_EH': results_gym_no_EH,
            'results_my_EH': results_my_EH,
            'results_gym_EH': results_gym_EH,
            'ratio_results_my': ratio_results_my,
            'ratio_results_gym': ratio_results_gym}


##################################################################################################################

def run_parameter_gridsize_tests():
    test_total_timesteps_grid5_m1 = [10000, 20000, 50000]
    test_episodes_grid5_m1 = [500, 1000, 2000]
    test_max_timesteps_grid5_m1 = [50, 100]
    test_total_timesteps_grid5_m2 = [20000, 50000]
    test_episodes_grid5_m2 = [1000, 2000, 3000]
    test_max_timesteps_grid5_m2 = [100, 200]
    # Standard model 1 - Gridsize 5
    run_parameter_gridsize_test_gym_env(1, 5, test_total_timesteps_grid5_m1)
    #run_parameter_gridsize_test_my_env(1, 5, test_episodes_grid5_m1, test_max_timesteps_grid5_m1)
    # Standard model 2 - Gridsize 5
    run_parameter_gridsize_test_gym_env(2, 5, test_total_timesteps_grid5_m2)
    #run_parameter_gridsize_test_my_env(2, 5, test_episodes_grid5_m2, test_max_timesteps_grid5_m2)

    test_total_timesteps_grid20_m1 = [20000, 50000]
    test_episodes_grid20_m1 = [1000, 5000, 10000]
    test_max_timesteps_grid20_m1 = [100, 200]
    test_total_timesteps_grid20_m2 = [50000, 100000]
    test_episodes_grid20_m2 = [5000, 10000, 20000]
    test_max_timesteps_grid20_m2 = [200, 400]
    # Standard model 1 - Gridsize 5
    run_parameter_gridsize_test_gym_env(1, 20, test_total_timesteps_grid20_m1)
    run_parameter_gridsize_test_my_env(1, 20, test_episodes_grid20_m1, test_max_timesteps_grid20_m1)
    # Standard model 2 - Gridsize 5
    run_parameter_gridsize_test_gym_env(2, 20, test_total_timesteps_grid20_m2)
    run_parameter_gridsize_test_my_env(2, 20, test_episodes_grid20_m2, test_max_timesteps_grid20_m2)


def run_parameter_gridsize_test_gym_env(model, gridsize, test_total_timesteps):
    if model == 1:
        csv_file = "param_test_model1_gridsize=" + str(gridsize) + '_gym_env.csv'
        if gridsize == 5:
            grid, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
        else:
            grid, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
        reward_param = reward_param_standard_model_1
    elif model == 2:
        csv_file = "param_test_model2_gridsize=" + str(gridsize) + '_gym_env.csv'
        if gridsize == 5:
            grid, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_2()
        else:
            grid, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
        reward_param = reward_param_standard_model_2
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Total Timesteps', 'EH_False', 'EHF_number_failures', 'EHF_number_successes',
                         'EHF_avg_path_length', 'EHF_avg_reward', 'EHF_avg_EH', 'EH_True', 'EHT_number_failures',
                         'EHT_number_successes', 'EHT_avg_path_length', 'EHT_avg_reward', 'EHT_avg_EH'])

        for total_timesteps in test_total_timesteps:
            file_name = "model_" + str(model) + "_grid_size=" + str(gridsize)
            results_gym_no_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles,
                                             lightsources=lightsources,
                                             use_EH=False, reward_param=reward_param, reward_weight=reward_weight,
                                             range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)
            results_gym_EH = test_gym_env(gridsize=gridsize, goals=goals, obstacles=obstacles,
                                          lightsources=lightsources,
                                          use_EH=True, reward_param=reward_param, reward_weight=reward_weight,
                                          range_EH=range_EH, timesteps=total_timesteps, file_name=file_name)

            writer.writerow([
                str(total_timesteps),
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


def run_parameter_gridsize_test_my_env(model, gridsize, test_episodes, test_max_timesteps):
    if model == 1:
        csv_file = "param_test_model1_gridsize=" + str(gridsize) + '_my_env.csv'
        if gridsize == 5:
            grid, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_1()
        else:
            grid, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_1()
        reward_param = reward_param_standard_model_1
    elif model == 2:
        csv_file = "param_test_model2_gridsize=" + str(gridsize) + '_my_env.csv'
        if gridsize == 5:
            grid, goals, obstacles, lightsources, reward_weight, range_EH = generate_small_model_2()
        else:
            grid, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()
        reward_param = reward_param_standard_model_2
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Episodes', 'Max Timesteps', 'EH_False', 'EHF_number_failures', 'EHF_number_successes',
                         'EHF_avg_path_length', 'EHF_avg_reward', 'EHF_avg_EH', 'EH_True', 'EHT_number_failures',
                         'EHT_number_successes', 'EHT_avg_path_length', 'EHT_avg_reward', 'EHT_avg_EH'])
        for episodes in test_episodes:
            for max_timesteps in test_max_timesteps:
                results_my_no_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles,
                                               lightsources=lightsources,
                                               use_EH=False, reward_param=reward_param, reward_weight=reward_weight,
                                               range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)
                results_my_EH = test_my_env(gridsize=gridsize, goals=goals, obstacles=obstacles,
                                            lightsources=lightsources,
                                            use_EH=True, reward_param=reward_param, reward_weight=reward_weight,
                                            range_EH=range_EH, episodes=episodes, max_timesteps=max_timesteps)

                writer.writerow([
                    str(episodes),
                    str(max_timesteps),
                    'False',
                    str(results_my_no_EH['number_failures']),
                    str(results_my_no_EH['number_successes']),
                    str(results_my_no_EH['avg_path_length']),
                    str(results_my_no_EH['avg_reward']),
                    str(results_my_no_EH['avg_EH']),
                    'True',
                    str(results_my_EH['number_failures']),
                    str(results_my_EH['number_successes']),
                    str(results_my_EH['avg_path_length']),
                    str(results_my_EH['avg_reward']),
                    str(results_my_EH['avg_EH'])
                ])
