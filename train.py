from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from gym_environment import *


def train_gym_env(env, total_timesteps, file_name):
    # Train the model
    model = PPO('MultiInputPolicy', env, verbose=0)
    model.learn(total_timesteps=total_timesteps)

    # Save the model
    model.save(file_name)

    return model


def train_my_env(env, num_episodes=10000, max_time_steps=1000):
    for episode in range(num_episodes):
        # initialise a random start position for each robot
        env.reset()

        # Iterate until we reached the end or we exceed the nr of max time steps
        for time_step in range(max_time_steps):

            # Loop over the robots > each robot has its own Q-Learning Agent
            for robot in env.robots:

                # Check if the current robot has already reached its goal
                if robot.is_done():
                    # If the current robot reached the goal already, it doesn't need to do anything anymore
                    break

                # The state for this robots' Q-Learning Agent is simply its position
                state = robot.position

                # get action (e-greedy action)
                action = robot.q_learn_agent.act(state)

                next_state, reward = env.step(robot, action)

                robot.q_learn_agent.learn(state, action, reward, next_state)
            if env.done():
                break
    return env
