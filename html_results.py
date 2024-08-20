import jinja2


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


def write_paths_to_html(output_file, env, paths):
    colors = ['limegreen', 'blue', 'red']

    with open(output_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n<head>\n')
        f.write('<title>Paths</title>\n')
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

        f.write('<h1 style="text-align: center"> For {} Robot(s)'.format(env.num_robots))
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


def write_results_to_html(output_file, results, kind_of_test):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    if kind_of_test == 'gridsize':
        # load the template
        template = env.get_template('template_gridsize_testresults.html')

    elif kind_of_test == 'multirobot':
        # load the template
        template = env.get_template('template_multirobot_testresults.html')

    elif kind_of_test == 'lightsource':
        # load the template
        template = env.get_template('template_lightsource_testresults.html')

    else:
        print("HTML file has FAILED to generate. No template for given kind of test")
        return

    # Render the template with the data
    rendered_html = template.render(data=results)
    with open(output_file, "w") as file:
        file.write(rendered_html)
    print("HTML file has been generated successfully.")
