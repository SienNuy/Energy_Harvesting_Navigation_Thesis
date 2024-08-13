from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import time
from gym_environment import *

# Predefined parameters for the environment
obstacles = [(2, 2), (3, 5), (5, 7), (8, 4)]
lightsources = [(2, 5), (5, 5), (8, 5)]
goals = [(7, 2)]
num_robots = len(goals)
grid_size = 10

# Build Env
env = MultiRobotEnv(grid_size=grid_size, num_robots=num_robots, goals=goals, obstacles=obstacles, lightsources=lightsources, use_EH=True, render_mode='human')

# Wrap environment in DummyVecEnv to handle multiple envs
env = DummyVecEnv([lambda: env])

# Train the model
model = PPO('MultiInputPolicy', env, verbose=0)
model.learn(total_timesteps=50000)

file_name = "env_" + str(num_robots) + '_robot_' + str(grid_size) + 'x' + str(grid_size) + '_EH'

# Save the model
model.save(file_name)

# Load the model
model = PPO.load(file_name)

number_failures = 0
number_successes = 0

avg_path_length = 0
avg_EH = 0
avg_reward = 0

# Run the model 50 times and render the output
for _ in range(50):
    obs = env.reset()
    env.render()

    path_length = 0
    reward = 0
    EH = 0

    # Max 50 steps
    for i in range(50):
        print(str(i))
        actions, _states = model.predict(obs, deterministic=False)
        obs, rewards, done, info = env.step(actions)
        env.render()
        time.sleep(0.5)

        path_length += 1
        reward += rewards[0]
        EH += obs['harvested_energy'][0]
        if done:
            print('DONE')
            number_successes += 1

            avg_path_length += path_length
            avg_EH += EH
            avg_reward += reward

            break
    if not done:
        number_failures += 1


env.close()
print("failures = " + str(number_failures))
print("successes = " + str(number_successes))
print("avg path length = " + str(avg_path_length/50))
print("avg reward = " + str(avg_reward/50))
print("avg EH = " + str(avg_EH/50))


