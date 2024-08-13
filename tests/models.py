from my_environment.my_robot import Robot
from my_environment.my_environment import Environment
from gym_environment import MultiRobotEnv


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


def build_gym_environment(gridsize, goals, obstacles, lightsources, use_EH):
    env = MultiRobotEnv(grid_size=gridsize, num_robots=len(goals), goals=goals, obstacles=obstacles,
                        lightsources=lightsources, use_EH=use_EH, render_mode='human')

    return env


def generate_standard_model_1():
    gridsize = 10
    goals = [(7, 2)]
    obstacles = [(3, 3), (5, 7), (8, 4)]
    lightsources = [(2, 5), (5, 5), (8, 5)]
    return gridsize, goals, obstacles, lightsources


def generate_standard_model_2():
    gridsize = 10
    goals = [(7, 2), (1, 1)]
    obstacles = [(3, 3), (5, 7), (8, 4)]
    lightsources = [(2, 5), (5, 5), (8, 5)]
    return gridsize, goals, obstacles, lightsources


