from q_agent import QLearningAgent
import numpy as np


class Robot:
    def __init__(self, _id, goal, action_size=4):
        self.id = _id
        self.goal = goal
        self.harvested_energy = 0

        self.position = None
        self.env = None
        self.q_learn_agent = None

        self.init_q_learn_agent(action_size)

    def init_q_learn_agent(self, action_size):
        self.q_learn_agent = QLearningAgent(action_size=action_size)

    def connect_with_environment(self, environment):
        self.env = environment

    def reset(self, start_position):
        """
        Reset the robot to a given starting position and harvested energy will be reset to 0
        :param start_position: (x, y) position from where the robot will start to get to the goal
        """
        self.position = start_position
        self.harvested_energy = 0

    def is_done(self):
        return self.position == self.goal

    def move(self, action):
        x, y = self.position
        if action == 0:  # Up
            y = y - 1
        elif action == 1:  # Down
            y = y + 1
        elif action == 2:  # Left
            x = x - 1
        elif action == 3:  # Right
            x = x + 1

        if self.is_valid_position((x, y)) and not self.causes_collision((x, y)):  # and not (x, y) in self.observe_other_robots_goals():
            self.position = (x, y)

        return self.is_valid_position((x, y)), self.causes_collision((x, y))

    def is_valid_position(self, position):
        """
        Check if the new position of the robot is valid:
            * no collision with walls
        """
        x, y = position
        if x < 0 or x >= self.env.width or y < 0 or y >= self.env.height:
            return False

        return True

    def causes_collision(self, position):
        """
        Check if a collision occurs if the robot would move to that position
            * no collision with obstacles
            * no collision with other robots
        """
        # Check for collisions with obstacles
        if position in self.observe_obstacles():
            return True

        # Check for collisions with other robots
        if position in self.observe_other_robots_positions():
            return True

        return False

    def too_close_to_other_robots(self):
        for other_position in self.observe_other_robots_positions():
            diff = abs(self.position[0] - other_position[0]) + abs(self.position[1] - other_position[1])
            if diff <= 1:
                return True
        return False

    def observe_other_robots_positions(self):
        return [r.position for r in self.env.robots if r.id != self.id]

    def observe_other_robots_goals(self):
        return [r.goal for r in self.env.robots if r.id != self.id]

    def observe_obstacles(self):
        return self.env.obstacles

    def observe_lightsources(self):
        return self.env.lightsources

    def calculate_distances_to_lightsource(self):
        """
        Calculate the Eucledian distances between the robot and each of the lightsources
        """
        distances = []
        for lightsource in self.observe_lightsources():
            d = abs(self.position[0] - lightsource[0]) + abs(self.position[1] - lightsource[1])
            if d <= 3:
                distances.append(d)
            else:
                distances.append(None)
        return distances

    def calculate_energy_harvest(self):
        total_EH = 0
        distances = self.calculate_distances_to_lightsource()
        for distance in distances:
            if distance is not None:
                if distance == 0:
                    total_EH += 5
                else:
                    total_EH += 1/distance

        self.harvested_energy += total_EH
        return total_EH
