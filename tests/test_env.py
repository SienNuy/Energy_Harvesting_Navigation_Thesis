from tests.models import *
from train import *
from navigate_env import *
from stable_baselines3.common.vec_env import DummyVecEnv


def test_my_env(gridsize, goals, obstacles, lightsources, use_EH):
    # My Environment
    print('\nBuild My Env')
    # Build my environment
    my_env = build_my_environment(gridsize, goals, obstacles, lightsources, use_EH)

    # Train Qlearning
    print('Start Training My Env')
    my_env = train_my_env(my_env)
    print('Done Training My Env')

    # Navigate through the environment and get results
    number_failures, number_successes, avg_path_length, avg_reward, avg_EH = navigate_my_env(my_env)


def test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, timesteps):
    # Gym Environment
    print('\nBuild Gym Env')
    # Build gym environment
    gym_env = build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH)

    # Wrap environment in DummyVecEnv to handle multiple envs
    gym_env = DummyVecEnv([lambda: gym_env])

    file_name = 'models/' + ((str(gridsize)) + 'x' + str(gridsize) + '_' + str(len(goals)) + '_robots_' +
                 str(len(obstacles)) + '_obs_' + str(len(lightsources)) + '_lights')
    if use_EH:
        file_name += '_EH'

    # Train PPO
    print('Start Training Gym Env')
    model = train_gym_env(gym_env, timesteps, file_name)
    print('Done Training Gym Env')

    # Navigate through the environment and get results
    number_failures, number_successes, avg_path_length, avg_reward, avg_EH = navigate_gym_env(gym_env, model)

