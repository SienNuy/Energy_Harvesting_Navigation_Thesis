import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pygame


class MultiRobotEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, grid_size=None, num_robots=None, goals=None, obstacles=None, use_EH=True, lightsources=None,
                 reward_param=None, reward_weight=None, range_EH=None, render_mode=None):
        super(MultiRobotEnv, self).__init__()

        self.grid_size = grid_size
        self.num_robots = num_robots
        self.goals = np.array(goals, dtype=np.int32)
        self.obstacles = obstacles
        self.use_EH = use_EH
        self.lightsources = lightsources
        self.reward_param = reward_param
        self.reward_weight = reward_weight
        self.range_EH = range_EH

        # Define the action and observation space
        self.action_space = spaces.MultiDiscrete([4] * self.num_robots)
        self.observation_space = spaces.Dict({
            'robots': spaces.Box(low=0, high=self.grid_size - 1, shape=(self.num_robots, 2), dtype=np.int32),
            'goals': spaces.Box(low=0, high=self.grid_size - 1, shape=(self.num_robots, 2), dtype=np.int32),
            'obstacles': spaces.Box(low=0, high=self.grid_size - 1, shape=(len(self.obstacles), 2), dtype=np.int32),
            'lightsources': spaces.Box(low=0, high=self.grid_size - 1, shape=(len(self.lightsources), 2), dtype=np.int32),
        })

        # Rendering
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode
        # Pygame initialization
        self.cell_size = 50
        if self.render_mode == "human":
            pygame.init()
            self.screen = pygame.display.set_mode((self.grid_size * self.cell_size, self.grid_size * self.cell_size))
            pygame.display.set_caption("Multi-Robot Environment")

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        # Place robots
        self.robots = []
        for i in range(self.num_robots):
            while True:
                pos = (np.random.randint(self.grid_size), np.random.randint(self.grid_size))
                if pos not in self.obstacles and pos not in self.robots and pos not in self.goals:
                    self.robots.append(pos)
                    break
        self.robots = np.array(self.robots, dtype=np.int32)
        self.harvested_energy = np.zeros(self.num_robots, dtype=np.float32)

        # Return initial observation (robot positions) and an empty info dictionary
        return self._get_observation(), {}

    def _get_observation(self):
        return {
            'robots': self.robots.copy(),
            'goals': self.goals.copy(),
            'obstacles': self.obstacles.copy(),
            'lightsources': self.lightsources.copy(),
        }

    def step(self, actions):
        total_reward = 0
        nr_of_done = 0
        for i in range(self.num_robots):

            # Check if robot is already done
            if self.is_robot_done(i):
                nr_of_done += 1

            # Otherwise move robot
            else:
                is_valid_move, causes_collision = self.move_robot(i, actions[i])
                total_EH = self.calculate_energy_harvest(i)
                self.harvested_energy[i] += total_EH
                total_reward += self.get_reward(i, is_valid_move, causes_collision, total_EH)
                if self.is_robot_done(i):
                    nr_of_done += 1

        obs = self._get_observation()
        done = False
        if nr_of_done == self.num_robots:
            done = True

        return obs, total_reward, done, False, {'EH': self.harvested_energy}

    def move_robot(self, robot_id, action):
        new_position = self.robots[robot_id].copy()  # Use .copy() to avoid modifying the original array
        if action == 0:  # Up
            new_position[0] -= 1
        elif action == 1:  # Down
            new_position[0] += 1
        elif action == 2:  # Left
            new_position[1] -= 1
        elif action == 3:  # Right
            new_position[1] += 1

        if self.is_valid_position(new_position) and not self.causes_collision(new_position, robot_id):
            self.robots[robot_id] = new_position  # If no collision, take the actual step

        return self.is_valid_position(new_position), self.causes_collision(new_position, robot_id)

    def is_valid_position(self, position):
        """
        Check if the new position of the robot is valid:
            * no collision with walls
        """
        # Check if out of bounds
        if position[0] < 0 or position[1] < 0 or position[0] >= self.grid_size or position[1] >= self.grid_size:
            return False
        return True

    def causes_collision(self, position, robot_id):
        """
        Check if a collision occurs if the robot would move to that position
            * no collision with obstacles
            * no collision with other robots
        """
        # Check for collisions with obstacles
        if tuple(position) in self.obstacles:
            return True

        # Check for collisions with other robots
        for i, robot_position in enumerate(self.robots):
            if i != robot_id:
                if np.array_equal(position, robot_position):
                    return True
        return False

    def calculate_distances_to_lightsource(self, robot_id):
        position = self.robots[robot_id].copy()
        distances = []
        for lightsource in self.lightsources:
            d = abs(position[0] - lightsource[0]) + abs(position[1] - lightsource[1])
            if d <= self.range_EH:
                distances.append(d)
            else:
                distances.append(None)
        return distances

    def calculate_energy_harvest(self, robot_id):
        total_EH = 0
        distances = self.calculate_distances_to_lightsource(robot_id)
        for distance in distances:
            if distance is not None:
                if distance == 0:
                    total_EH += self.reward_param['reward_EH']
                else:
                    total_EH += 1/(distance ** self.reward_param['reward_EH_power'])
        return total_EH

    def get_reward(self, robot_id, is_valid_move, causes_collision, total_EH):
        move_reward = self.get_move_reward(robot_id, is_valid_move, causes_collision)
        if self.use_EH:
            weighted_reward = self.reward_weight * move_reward + (1-self.reward_weight) * total_EH
            return weighted_reward
        return move_reward

    def get_move_reward(self, robot_id, is_valid_move, causes_collision):
        if self.is_robot_done(robot_id):
            #reward = 1000
            reward = self.reward_param['reward_done']
        elif not is_valid_move:
            #reward = -2
            reward = self.reward_param['penalty_invalid_move']
        elif causes_collision:
            #reward = -5
            reward = self.reward_param['penalty_collision']
        else:
            #reward = -0.2
            reward = self.reward_param['penalty_move']
        return reward

    def is_robot_done(self, robot_id):
        # Check if the robot reached its goal
        if np.array_equal(self.robots[robot_id], self.goals[robot_id]):
            return True
        return False

    def render(self):
        if self.render_mode == 'human':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.fill((255, 255, 255))  # White background

            # Draw grid
            for x in range(0, self.grid_size * self.cell_size, self.cell_size):
                for y in range(0, self.grid_size * self.cell_size, self.cell_size):
                    rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

            # Draw obstacles
            for (i, j) in self.obstacles:
                rect = pygame.Rect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect)

            # Draw lightsources
            for (i, j) in self.lightsources:
                rect = pygame.Rect(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (255, 255, 0), rect)

            # Draw robots
            for i, (x, y) in enumerate(self.robots):
                pygame.draw.circle(self.screen, (0, 0, 255),
                                   (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2),
                                   self.cell_size // 3)
                font = pygame.font.SysFont(None, 24)
                img = font.render(str(i), True, (255, 255, 255))
                self.screen.blit(img, (x * self.cell_size + self.cell_size // 2 - img.get_width() // 2,
                                       y * self.cell_size + self.cell_size // 2 - img.get_height() // 2))

            # Draw goals
            for i, (x, y) in enumerate(self.goals):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (255, 0, 0), rect, 2)
                font = pygame.font.SysFont(None, 24)
                img = font.render(str(i), True, (255, 0, 0))
                self.screen.blit(img, (x * self.cell_size + self.cell_size // 2 - img.get_width() // 2,
                                       y * self.cell_size + self.cell_size // 2 - img.get_height() // 2))

            pygame.display.flip()

    def close(self):
        if self.render_mode == 'human':
            pygame.quit()
