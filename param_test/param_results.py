#########################################################################################################
# Standard Model 1
reward_param_standard_model_1 = {
    'reward_done': 100,
    'penalty_invalid_move': -2,
    'penalty_collision': -5,
    'penalty_move': -0.2,
    'reward_EH': 5,
    'reward_EH_power': 2,
}

total_timesteps_standard_model_1 = 50000
episodes_standard_model_1 = 1000
max_timesteps_standard_model_1 = 100


# Standard Model 2
reward_param_standard_model_2 = {
    'reward_done': 1000,
    'penalty_invalid_move': -5,
    'penalty_collision': -2,
    'penalty_move': -0.2,
    'reward_EH': 5,
    'reward_EH_power': 2,
}

total_timesteps_standard_model_2 = 100000
episodes_standard_model_2 = 10000
max_timesteps_standard_model_2 = 200

#########################################################################################################
# TESTS
# Grid size
total_timesteps_gridsize_5_model_1 = 20000
episodes_gridsize_5_model_1 = 2000
max_timesteps_gridsize_5_model_1 = 100

total_timesteps_gridsize_5_model_2 = 50000
episodes_gridsize_5_model_2 = 3000
max_timesteps_gridsize_5_model_2 = 100

total_timesteps_gridsize_20_model_1 = 20000
episodes_gridsize_20_model_1 = 1000
max_timesteps_gridsize_20_model_1 = 100

total_timesteps_gridsize_20_model_2 = 100000
episodes_gridsize_20_model_2 = 5000
max_timesteps_gridsize_20_model_2 = 200

# Lightsources
reward_param_lights_1_model_1 = reward_param_standard_model_1
reward_param_lights_1_model_1['reward_EH'] = 3
reward_param_lights_1_model_1['reward_EH_power'] = 2

reward_param_lights_1_model_2 = reward_param_standard_model_2
reward_param_lights_1_model_2['reward_EH'] = 3
reward_param_lights_1_model_2['reward_EH_power'] = 2

reward_param_lights_7_model_1 = reward_param_standard_model_1
reward_param_lights_7_model_1['reward_EH'] = 2
reward_param_lights_7_model_1['reward_EH_power'] = 2

reward_param_lights_7_model_2 = reward_param_standard_model_2
reward_param_lights_7_model_2['reward_EH'] = 10
reward_param_lights_7_model_2['reward_EH_power'] = 2

reward_param_lights_7_clust_model_1 = reward_param_standard_model_1
reward_param_lights_7_clust_model_1['reward_EH'] = 0
reward_param_lights_7_clust_model_1['reward_EH_power'] = 0

reward_param_lights_7_clust_model_2 = reward_param_standard_model_2
reward_param_lights_7_clust_model_2['reward_EH'] = 5
reward_param_lights_7_clust_model_2['reward_EH_power'] = 2



