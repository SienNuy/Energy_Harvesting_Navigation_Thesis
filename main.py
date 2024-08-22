from tests.multi_robot_tests import run_all_multi_robot_tests
from tests.gridsize_tests import run_all_gridsize_tests, run_parameter_gridsize_tests
from tests.lightsource_tests import run_all_lightsource_tests, run_parameter_lightsource_tests
from tests.reward_weights_tests import run_all_reward_weights_tests
from tests.range_EH_tests import run_all_range_EH_tests
from html_results import *

# PARAM TEST SCENARIOS
#run_parameter_gridsize_tests()
run_parameter_lightsource_tests()


# MULTI ROBOT TEST
#my_envs, multi_robot_tests_results = run_all_multi_robot_tests()

#write_results_to_html("multi_robot_tests.html", multi_robot_tests_results, 'multirobot')


# GRIDSIZE TEST
#gridsize_tests_results = run_all_gridsize_tests()

#write_results_to_html("gridsize_tests.html", gridsize_tests_results, 'gridsize')


# LIGHTSOURCE TEST
#lightsource_tests_results = run_all_lightsource_tests()

#write_results_to_html("lightsource_tests.html", lightsource_tests_results, 'lightsource')


#reward_weights_tests_results = run_all_reward_weights_tests()

#range_EH_tests_results = run_all_range_EH_tests()
