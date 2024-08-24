from tests.multi_robot_tests import run_all_multi_robot_tests
from tests.gridsize_tests import run_all_gridsize_tests, run_parameter_gridsize_tests
from tests.lightsource_tests import run_all_lightsource_tests, run_parameter_lightsource_tests
from tests.reward_weights_tests import run_all_reward_weights_tests
from tests.range_EH_tests import run_all_range_EH_tests
from html_results import *
from tests.utils.models import generate_standard_model_2

# PARAM TEST SCENARIOS
run_parameter_gridsize_tests()
run_parameter_lightsource_tests()

#gridsize, goals, obstacles, lightsources, reward_weight, range_EH = generate_standard_model_2()

# MULTI ROBOT TEST
#my_envs, my_paths, multi_robot_tests_results = run_all_multi_robot_tests()
#for key, path_info in my_paths.items():
#    file = "results/multi_robot_paths" + str(key) + ".html"
#    write_path_to_html2(file, 2, path_info, obstacles, lightsources, goals)
#write_results_to_html("results/multi_robot_tests.html", multi_robot_tests_results, 'multirobot')


# GRIDSIZE TEST
#gridsize_tests_results = run_all_gridsize_tests()

#write_results_to_html("gridsize_tests.html", gridsize_tests_results, 'gridsize')


# LIGHTSOURCE TEST
#lightsource_tests_results = run_all_lightsource_tests()

#write_results_to_html("lightsource_tests.html", lightsource_tests_results, 'lightsource')


#reward_weights_tests_results = run_all_reward_weights_tests()
#write_results_to_html("reward_weight_tests.html", reward_weights_tests_results, 'weight')


#range_EH_tests_results = run_all_range_EH_tests()
#write_results_to_html("range_EH_tests.html", range_EH_tests_results, 'range')

