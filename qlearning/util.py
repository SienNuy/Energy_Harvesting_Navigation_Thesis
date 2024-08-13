from random import randrange

import numpy as np


def write_q_table_to_html(output_file, env):
    with open(output_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n<head>\n')
        f.write('<title>QTable</title>\n')
        f.write('<style>\n'
                '\ttable {\n'
                '\t\tborder-collapse: collapse;\n'
                '\t\tmargin: 20px auto;\n'
                '\t}\n'
                '\ttd {\n'
                '\t\twidth: 80px;\n'
                '\t\theight: 80px;\n'
                '\t\tborder: 1px solid black;\n'
                '\t\ttext-align: center;\n'
                '\t\tvertical-align: middle;\n'
                '\t\tposition: relative;\n'
                '\t}\n'
                '\t.arrow {\n'
                '\t\tposition: absolute;\n'
                '\t\tfont-size: 10px;\n'
                '\t}\n'
                '\t.up {\n'
                '\t\ttop: 2px;\n'
                '\t\tleft: 50%;\n'
                '\t\ttransform: translateX(-50%);\n'
                '\t}\n'
                '\t.down {\n'
                '\t\tbottom: 2px;\n'
                '\t\tleft: 50%;\n'
                '\t\ttransform: translateX(-50%);\n'
                '\t}\n'
                '\t.left {\n'
                '\t\ttop: 50%;\n'
                '\t\tleft: 2px;\n'
                '\t\ttransform: translateY(-50%);\n'
                '\t}\n'
                '\t.right {\n'
                '\t\ttop: 50%;\n'
                '\t\tright: 2px;\n'
                '\t\ttransform: translateY(-50%);\n'
                '\t}\n'
                '\t.green {\n'
                '\t\tcolor: limegreen;\n'
                '\t}\n'
                '\t.red {\n'
                '\t\tcolor: red;\n'
                '\t}\n'
                '</style>\n')
        f.write('</head>\n<body>\n')
        for robot in env.robots:
            f.write('<h1 style="text-align: center"> Robot {}'.format(robot.id))
            if env.use_EH:
                f.write(' - Energy Harvesting')
            f.write('</h1>\n')
            f.write('<table>\n')
            f.write('<tbody>\n')
            q_table = robot.q_learn_agent.q_table
            for h in range(env.height):
                f.write('<tr>\n')
                for w in range(env.width):
                    position = (w, h)
                    if position in env.lightbulbs:
                        f.write('<td style="background-color: yellow">\n')
                    else:
                        f.write('<td>\n')
                    if position in env.obstacles:
                        f.write('<div> X </div>')
                    if position == robot.goal:
                        f.write('<div> GOAL </div>')
                    if position in q_table:
                        q_values = q_table[position]
                        highest_value = q_values.max()
                        if q_values[0] != float('-inf'):
                            if q_values[0] == highest_value:
                                f.write('<div class="arrow up green">&uarr;')
                            elif q_values[0] < 0:
                                f.write('<div class="arrow up red">&uarr;')
                            else:
                                f.write('<div class="arrow up">&uarr;')
                            f.write('{:.2f}'.format(q_values[0]))
                            f.write('</div>\n')

                        if q_values[1] != float('-inf'):
                            if q_values[1] == highest_value:
                                f.write('<div class="arrow down green">&darr;')
                            elif q_values[1] < 0:
                                f.write('<div class="arrow down red">&darr;')
                            else:
                                f.write('<div class="arrow down">&darr;')
                            f.write('{:.2f}'.format(q_values[1]))
                            f.write('</div>\n')

                        if q_values[2] != float('-inf'):
                            if q_values[2] == highest_value:
                                f.write('<div class="arrow left green">&larr;')
                            elif q_values[2] < 0:
                                f.write('<div class="arrow left red">&larr;')
                            else:
                                f.write('<div class="arrow left">&larr;')
                            f.write('{:.2f}'.format(q_values[2]))
                            f.write('</div>\n')

                        if q_values[3] != float('-inf'):
                            if q_values[3] == highest_value:
                                f.write('<div class="arrow right green">&rarr;')
                            elif q_values[3] < 0:
                                f.write('<div class="arrow right red">&rarr;')
                            else:
                                f.write('<div class="arrow right">&rarr;')
                            f.write('{:.2f}'.format(q_values[3]))
                            f.write('</div>\n')
                    f.write('</td>\n')
                f.write('</tr>\n')
            f.write('</tbody>\n')
            f.write('</table>\n')
        f.write('</body>\n</html>')
    print("HTML file has been generated successfully.")


def generate_starting_points(env):
    starting_points = []
    for _ in range(5):
        starting_point = []
        for r in range(env.num_robots):
            while True:
                x = randrange(0, env.width)
                y = randrange(0, env.height)
                if ((x, y) not in starting_point and env.robots[r].is_valid_position((x, y))
                        and (x, y) != env.robots[r].goal):
                    break
            starting_point.append((x, y))
        starting_points.append(starting_point)
    return starting_points


def navigate_paths(env):
    paths = []
    rewards = []
    starting_points = generate_starting_points(env)
    for starting_point in starting_points:  # starting point contains a starting position for each robot
        path = {}
        total_reward = {}
        # init robots into their respective start positions
        for i, robot in enumerate(env.robots):
            robot.reset(starting_point[i])
            path[robot.id] = [robot.position]
            total_reward[robot.id] = 0

        # keep looping until all robots finished
        while True:
            for robot in env.robots:
                if robot.is_done():
                    continue
                # get the best action of the robot based on their q_table
                q_table = robot.q_learn_agent.q_table
                state = robot.position
                q_values = q_table[state]
                best_action = np.argmax(q_values)
                next_state, reward = env.step(robot, best_action)
                if next_state == state:
                    if reward == -15:  # collision so choose next best action
                        # go on with second best action
                        # Get the indices that would sort the array
                        sorted_indices = np.argsort(q_values)
                        # get second_best_action
                        second_best_action = sorted_indices[-2]
                        next_state, reward = env.step(robot, second_best_action)
                        print('COLLISION AVOIDANCE')
                    else:
                        print('ERROR something went wrong finding the path')

                elif next_state in path[robot.id]:
                    print('ERROR We has a situation where we would go back to a previous state')
                    # go on with second best action
                    # reset robot to the current state
                    robot.position = state
                    # Get the indices that would sort the array
                    sorted_indices = np.argsort(q_values)
                    # get second_best_action
                    second_best_action = sorted_indices[-2]
                    next_state, reward = env.step(robot, second_best_action)

                path[robot.id].append(next_state)
                total_reward[robot.id] += reward

            if env.done():
                paths.append(path)
                rewards.append(total_reward)
                break
    return paths, rewards


def write_results_to_html(output_file, env, paths, rewards):
    colors = ['limegreen', 'blue', 'red']

    with open(output_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n<head>\n')
        f.write('<title>Results</title>\n')
        f.write('<style>\n'
                '\ttable {\n'
                '\t\tborder-collapse: collapse;\n'
                '\t\tmargin: 20px auto;\n'
                '\t}\n'
                '\ttd {\n'
                '\t\twidth: 30px;\n'
                '\t\theight: 30px;\n'
                '\t\tborder: 1px solid black;\n'
                '\t\ttext-align: center;\n'
                '\t\tvertical-align: middle;\n'
                '\t\tposition: relative;\n'
                '\t}\n'
                '</style>\n')
        f.write('</head>\n<body>\n')

        f.write('<h1 style="text-align: center"> For {} Robots'.format(env.num_robots))
        if env.use_EH:
            f.write(' With Energy Harvesting')
        f.write('</h1>\n')

        for i, path_robots in enumerate(paths):
            f.write('<h2 style="text-align: center"> No{} path </h2>\n'.format(i))

            f.write('<table>\n')
            f.write('<tbody>\n')
            for h in range(env.height):
                f.write('<tr>\n')
                for w in range(env.width):
                    position = (w, h)
                    in_path = False
                    for robot_id, path in path_robots.items():
                        if position in path:
                            time_step = path.index(position)
                            if in_path:
                                # this means another path was also in this position, we simply add the time step
                                f.write('{}'.format(time_step))
                            else:
                                f.write('<td style="background-color: {}">\n '
                                        '<div> {} '.format(colors[robot_id], time_step))
                                in_path = True
                    if not in_path:
                        f.write('</div>\n <td>\n')
                    if position in env.obstacles:
                        f.write('<div> X </div>')

                    for robot in env.robots:
                        if position == robot.goal:
                            f.write('<div> GOAL </div>')
                    if position in env.lightbulbs:
                        f.write('<div style="background-color: yellow"> * </div>')
                    f.write('</td>\n')
                f.write('</tr>\n')
            f.write('</tbody>\n')
            f.write('</table>\n')
        f.write('</body>\n</html>')
    print("HTML file has been generated successfully.")
