from stable_baselines3 import PPO
import os


def train_gym_env(env, total_timesteps, file_name):
    file_name += '_timesteps=' + str(total_timesteps)
    zip_file = file_name + '.zip'

    if os.path.exists(file_name):
        print("Model file found. Loading the model...")
        # Load the model
        model = PPO.load(file_name, env=env)

    elif os.path.exists(zip_file):
        print("Model ZIP file found. Loading the model...")
        # Load the model
        model = PPO.load(file_name, env=env)
        model.save(file_name)

    else:
        print("Model file not found. Training a new model...")
        # Train the model
        model = PPO('MultiInputPolicy', env, verbose=0)
        model.learn(total_timesteps=total_timesteps)

        # Save the model
        model.save(file_name)

    return model


def train_my_env(env, episodes, max_timesteps):
    for episode in range(episodes):
        # initialise a random start position for each robot
        env.reset()

        # Iterate until we reach a terminal state, or we exceed the nr of max time steps
        for time_step in range(max_timesteps):

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

                next_state, reward, info = env.step(robot, action)

                robot.q_learn_agent.learn(state, action, reward, next_state)
            if env.done():
                break
    return env
