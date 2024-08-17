from tests.util.train_env import *
from tests.util.navigate_env import *
from stable_baselines3.common.vec_env import DummyVecEnv
from environment.my_environment.my_robot import Robot
from environment.my_environment.my_environment import Environment
from environment.gym_environment import MultiRobotEnv


def build_my_environment(gridsize, goals, obstacles, lightsources, use_EH):
    # Build Robots
    robots = []
    for i, goal in enumerate(goals):
        robot = Robot(_id=i, goal=goal)
        robots.append(robot)

    # Build Environment
    env = Environment(width=gridsize, height=gridsize, obstacles=obstacles, lightsources=lightsources, use_EH=use_EH)
    env.add_robots(robots)

    return env


def build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH, reward_param):
    env = MultiRobotEnv(grid_size=gridsize, num_robots=len(goals), goals=goals, obstacles=obstacles,
                        lightsources=lightsources, use_EH=use_EH, reward_param=reward_param, render_mode='human')

    return env


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

    return {'number_failures': number_failures,
            'number_successes': number_successes,
            'avg_path_length': avg_path_length,
            'avg_reward': avg_reward,
            'avg_EH': avg_EH}


def test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, reward_param, timesteps, sample_start_positions, file_name):
    # Gym Environment
    print('Build Gym Env')
    # Build gym environment
    gym_env = build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH, reward_param)

    # Wrap environment in DummyVecEnv to handle multiple envs
    gym_env = DummyVecEnv([lambda: gym_env])

    file_name = 'tests/models/' + file_name
    if use_EH:
        file_name += '_EH'

    # Train PPO
    print('Start Training Gym Env')
    model = train_gym_env(gym_env, timesteps, file_name)
    print('Done Training Gym Env')

    # Navigate through the environment and get results
    number_failures, number_successes, avg_path_length, avg_reward, avg_EH = navigate_gym_env(gym_env, model, sample_start_positions)

    return {'number_failures': number_failures,
            'number_successes': number_successes,
            'avg_path_length': avg_path_length,
            'avg_reward': avg_reward,
            'avg_EH': avg_EH}
