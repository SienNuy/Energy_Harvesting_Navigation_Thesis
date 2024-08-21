from tests.util.train_env import *
from tests.util.navigate_env import *
from stable_baselines3.common.vec_env import DummyVecEnv
from environment.my_environment.my_robot import Robot
from environment.my_environment.my_environment import Environment
from environment.gym_environment import MultiRobotEnv


def build_my_environment(gridsize, goals, obstacles, lightsources, use_EH, reward_param, reward_weight, range_EH):
    # Build Robots
    robots = []
    for i, goal in enumerate(goals):
        robot = Robot(_id=i, goal=goal)
        robots.append(robot)

    # Build Environment
    env = Environment(width=gridsize, height=gridsize, obstacles=obstacles, lightsources=lightsources, use_EH=use_EH,
                      reward_param=reward_param, reward_weight=reward_weight, range_EH=range_EH)
    env.add_robots(robots)

    return env


def build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH, reward_param, reward_weight, range_EH):
    env = MultiRobotEnv(grid_size=gridsize, num_robots=len(goals), goals=goals, obstacles=obstacles,
                        lightsources=lightsources, use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                        range_EH=range_EH, render_mode='human')

    return env


def test_my_env(gridsize, goals, obstacles, lightsources, use_EH, reward_param, reward_weight, range_EH, episodes, max_timesteps, num_start_positions=10, return_env=False):
    # My Environment
    print('\nBuild My Env')
    # Build my environment
    my_env = build_my_environment(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH)

    # Train Qlearning
    print('Start Training My Env')
    my_env = train_my_env(env=my_env, episodes=episodes, max_timesteps=max_timesteps)
    print('Done Training My Env')

    # Navigate through the environment and get results
    number_failures, number_successes, avg_path_length, avg_reward, avg_EH = navigate_my_env(my_env=my_env, num_start_positions=num_start_positions)

    info = {'number_failures': number_failures,
            'number_successes': number_successes,
            'avg_path_length': avg_path_length,
            'avg_reward': avg_reward,
            'avg_EH': avg_EH}

    if return_env:
        return my_env, info

    return info


def test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, reward_param, reward_weight, range_EH, timesteps, file_name, num_start_positions=10):
    # Gym Environment
    print('Build Gym Env')
    # Build gym environment
    gym_env = build_gym_environment(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                    use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                    range_EH=range_EH)

    # Wrap environment in DummyVecEnv to handle multiple envs
    gym_env = DummyVecEnv([lambda: gym_env])

    if use_EH:
        file_name += '_EH'

    # Train PPO
    print('Start Training Gym Env')
    model = train_gym_env(env=gym_env, total_timesteps=timesteps, file_name=file_name)
    print('Done Training Gym Env')

    # Navigate through the environment and get results
    number_failures, number_successes, avg_path_length, avg_reward, avg_EH = navigate_gym_env(gym_env=gym_env, model=model, num_robots=len(goals), gridsize=gridsize, num_start_positions=num_start_positions)

    return {'number_failures': number_failures,
            'number_successes': number_successes,
            'avg_path_length': avg_path_length,
            'avg_reward': avg_reward,
            'avg_EH': avg_EH}
