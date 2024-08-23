from tests.utils.train_env import *
from tests.utils.navigate_env import *
from stable_baselines3.common.vec_env import DummyVecEnv
from environment.my_environment.my_robot import Robot
from environment.my_environment.my_environment import Environment
from environment.gym_environment import MultiRobotEnv
import time


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
                        lightsources=lightsources, use_EH=use_EH, reward_param=reward_param,
                        reward_weight=reward_weight,
                        range_EH=range_EH, render_mode='human')

    return env


def test_my_env(gridsize, goals, obstacles, lightsources, use_EH, reward_param, reward_weight, range_EH, episodes,
                max_timesteps, num_start_positions=10, return_env=False, return_path_info=False, return_execution_times=False):
    start_time_build = time.time()
    # My Environment
    print('\nBuild My Env')
    # Build my environment
    my_env = build_my_environment(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                  use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                  range_EH=range_EH)
    end_time_build = time.time()

    start_time_learn = time.time()
    # Train Qlearning
    print('Start Training My Env')
    my_env = train_my_env(env=my_env, episodes=episodes, max_timesteps=max_timesteps)
    print('Done Training My Env')
    end_time_learn = time.time()

    start_time_test = time.time()
    # Navigate through the environment and get results
    number_failures, number_successes, avg_path_length, avg_reward, avg_EH, path_info = navigate_my_env(my_env=my_env,
                                                                                                        num_start_positions=num_start_positions)
    end_time_test = time.time()

    build_time = end_time_build - start_time_build
    train_time = end_time_learn - start_time_learn
    test_time = end_time_test - start_time_test
    execution_times = (build_time, train_time, test_time)

    info = {'number_failures': number_failures,
            'number_successes': number_successes,
            'avg_path_length': avg_path_length,
            'avg_reward': avg_reward,
            'avg_EH': avg_EH}

    if return_env:
        if return_path_info:
            if return_execution_times:
                return my_env, path_info, execution_times, info
            return my_env, path_info, info

        if return_execution_times:
            return my_env, execution_times, info
        return my_env, info

    if return_path_info:
        if execution_times:
            return path_info, execution_times, info
        return path_info, info

    if return_execution_times:
        return execution_times, info
    return info


def test_gym_env(gridsize, goals, obstacles, lightsources, use_EH, reward_param, reward_weight, range_EH, timesteps,
                 file_name, num_start_positions=10, return_path_info=False, return_execution_times=False):
    start_time_build = time.time()

    # Gym Environment
    print('Build Gym Env')
    # Build gym environment
    gym_env = build_gym_environment(gridsize=gridsize, goals=goals, obstacles=obstacles, lightsources=lightsources,
                                    use_EH=use_EH, reward_param=reward_param, reward_weight=reward_weight,
                                    range_EH=range_EH)

    # Wrap environment in DummyVecEnv to handle multiple envs
    gym_env = DummyVecEnv([lambda: gym_env])
    end_time_build = time.time()

    if use_EH:
        file_name += '_EH'

    start_time_learn = time.time()
    # Train PPO
    print('Start Training Gym Env')
    model = train_gym_env(env=gym_env, total_timesteps=timesteps, file_name=file_name)
    print('Done Training Gym Env')
    end_time_learn = time.time()

    start_time_test = time.time()
    # Navigate through the environment and get results
    number_failures, number_successes, avg_path_length, avg_reward, avg_EH, path_info = navigate_gym_env(
        gym_env=gym_env, model=model, num_robots=len(goals), gridsize=gridsize, num_start_positions=num_start_positions)
    end_time_test = time.time()

    build_time = end_time_build - start_time_build
    train_time = end_time_learn - start_time_learn
    test_time = end_time_test - start_time_test
    execution_times = (build_time, train_time, test_time)

    info = {'number_failures': number_failures,
            'number_successes': number_successes,
            'avg_path_length': avg_path_length,
            'avg_reward': avg_reward,
            'avg_EH': avg_EH}

    if return_path_info:
        if return_execution_times:
            return path_info, execution_times, info
        return path_info, info

    if return_execution_times:
        return execution_times, info
    return info

