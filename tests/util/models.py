
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


