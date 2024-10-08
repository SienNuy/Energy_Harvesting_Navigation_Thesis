import numpy as np
from random import randrange


class Environment:
    def __init__(self, width, height, obstacles, lightsources, reward_param, reward_weight, range_EH, use_EH=False):
        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.lightsources = lightsources
        self.use_EH = use_EH
        self.reward_param = reward_param
        self.reward_weight = reward_weight
        self.range_EH = range_EH

        self.robots = []
        self.num_robots = 0

    def add_robots(self, robots):
        for robot in robots:
            robot.connect_with_environment(self)
            self.robots.append(robot)
            self.num_robots += 1

    def reset(self):
        """
        Resets the start positions of each robot to a random position in the environment
        """
        for robot in self.robots:
            # pick random position
            while True:
                x = randrange(0, self.width)
                y = randrange(0, self.height)
                if robot.is_valid_position((x, y)) and (x, y) != robot.goal:
                    robot.reset((x, y))
                    break

    def step(self, robot, action):
        # First move Robot
        is_valid_move, causes_collision = self.move_robot(robot, action)

        # Then calculate energy harvest
        total_EH = robot.calculate_energy_harvest()

        # Calculate reward
        reward = self.get_reward(robot, is_valid_move, causes_collision, total_EH)

        next_state = robot.position

        info = {'causes_collision': causes_collision}

        return next_state, reward, info

    def move_robot(self, robot, action):
        """
        Move the corresponding robot in the environment based on the action
        """
        return robot.move(action)

    def get_reward(self, robot, is_valid_move, causes_collision, total_EH):
        """
        Get the reward for the given robot based on its current position
        """
        move_reward = self.get_move_reward(robot, is_valid_move, causes_collision)
        if self.use_EH:
            weighted_reward = self.reward_weight * move_reward + (1-self.reward_weight) * total_EH
            return weighted_reward
        return move_reward

    def get_move_reward(self, robot, is_valid_move, causes_collision):
        if robot.is_done():
            # reward = 1000
            reward = self.reward_param['reward_done']
        elif not is_valid_move:  # this means the action leads to an invalid position in the grid
            # reward = -2
            reward = self.reward_param['penalty_invalid_move']
        elif causes_collision:  # this means the action leads to a collision with another robot
            # reward = -5
            reward = self.reward_param['penalty_collision']
        else:
            # reward = -0.2
            reward = self.reward_param['penalty_move']
        return reward

    def done(self):
        """
        The environment is done when all robots have reached their goal
        """
        for robot in self.robots:
            if not robot.is_done():
                return False
        return True
