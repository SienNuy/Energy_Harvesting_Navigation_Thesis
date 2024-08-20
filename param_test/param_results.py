#########################################################################################################
# Standard Model 1
reward_param_standard_model_1 = {
    'reward_done': 100,
    'penalty_invalid_move': -5,
    'penalty_collision': -2,
    'penalty_move': -0.1,
    'reward_EH': 2,
    'reward_EH_power': 2,
}

training_timesteps_standard_model_1 = 50000
episodes_standard_model_1 = 1000
max_timesteps_standard_model_1 = 200


# Standard Model 2
reward_param_standard_model_2 = {
    'reward_done': 500,
    'penalty_invalid_move': -5,
    'penalty_collision': -2,
    'penalty_move': -0.2,
    'reward_EH': 5,
    'reward_EH_power': 1,
}

training_timesteps_standard_model_2 = 100000
episodes_standard_model_2 = 5000
max_timesteps_standard_model_2 = 100

#########################################################################################################
# TESTS
# Multi Robot
training_timesteps_multi_robot_3 = 0
episodes_multi_robot_3 = 0
max_timesteps_multi_robot_3 = 0

# Grid size
training_timesteps_gridsize_5_model_1 = 0
episodes_gridsize_5_model_1 = 0
max_timesteps_gridsize_5_model_1 = 0
training_timesteps_gridsize_5_model_2 = 0
episodes_gridsize_5_model_2 = 0
max_timesteps_gridsize_5_model_2 = 0

training_timesteps_gridsize_20_model_1 = 0
episodes_gridsize_20_model_1 = 0
max_timesteps_gridsize_20_model_1 = 0
training_timesteps_gridsize_20_model_2 = 0
episodes_gridsize_20_model_2 = 0
max_timesteps_gridsize_20_model_2 = 0

# Lightsources
reward_EH_lights_1_model_1 = {
    'reward_EH': 0,
    'reward_EH_power': 0,
}
reward_EH_lights_1_model_2 = {
    'reward_EH': 0,
    'reward_EH_power': 0,
}

reward_EH_lights_7_model_1 = {
    'reward_EH': 0,
    'reward_EH_power': 0,
}
reward_EH_lights_7_model_2 = {
    'reward_EH': 0,
    'reward_EH_power': 0,
}

reward_EH_lights_7_clust_model_1 = {
    'reward_EH': 0,
    'reward_EH_power': 0,
}
reward_EH_lights_7_clust_model_2 = {
    'reward_EH': 0,
    'reward_EH_power': 0,
}



