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


def write_paths_to_html(output_file, nr_of_robots, path_info):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.get_template('template_html/template_path_navigation.html')
    # Render the template with the data
    path_data = {'nr_of_robots': nr_of_robots, 'path_info': path_info}
    rendered_html = template.render(data=path_data)
    with open(output_file, "w") as file:
        file.write(rendered_html)
    print("HTML file has been generated successfully.")


def write_path_to_html2(output_file, nr_of_robots, path_data, obstacles, lightsources, goals):
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

        f.write('<h1 style="text-align: center"> For {} Robots </h1>\n'.format(nr_of_robots))

        for i, path_info in enumerate(path_data):
            start_str = ""
            for start_pos in path_info["start_positions"]:
                start_str += str(start_pos) + "  "
            f.write('<h2 style="text-align: center"> Start Positions:{} </h2>\n'.format(start_str))

            f.write('<table>\n')
            f.write('<tbody>\n')
            for x in range(path_info["gridsize"]):
                f.write('<tr>\n')
                for y in range(path_info["gridsize"]):
                    in_path1 = False
                    in_path2 = False
                    time_step1 = None
                    time_step2 = None
                    obstacle = False
                    lightsource = False
                    goal = False

                    for ts1, position1 in path_info["path1"].items():
                        if (x, y) == position1:
                            in_path1 = True
                            time_step1 = ts1

                    for ts2, position2 in path_info["path2"].items():
                        if (x, y) == position2:
                            in_path2 = True
                            time_step2 = ts2
                    if (x, y) in obstacles:
                        obstacle = True

                    if (x, y) in lightsources:
                        lightsource = True

                    if (x, y) in goals:
                        goal = True

                    if not in_path1 and not in_path2:
                        f.write('<td>')

                    elif in_path1 and in_path2:
                        f.write('<td style="background-color: limegreen">\n'
                                '<div> {} {} </div>\n'.format(time_step1, time_step2))
                    elif in_path1:
                        f.write('<td style="background-color: limegreen">\n'
                                '<div> {} </div>\n'.format(time_step1))
                    elif in_path2:
                        f.write('<td style="background-color: #0048ff">\n'
                                '<div> {} </div>\n'.format(time_step2))

                    if lightsource:
                        f.write('<div style="background-color: yellow"> * </div>')
                    if obstacle:
                        f.write('<div> X </div>')
                    if goal:
                        f.write('<div> GOAL </div>')
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
        template = env.get_template('template_html/template_gridsize_testresults.html')

    elif kind_of_test == 'multirobot':
        # load the template
        template = env.get_template('template_html/template_multirobot_testresults.html')

    elif kind_of_test == 'lightsource':
        # load the template
        template = env.get_template('template_html/template_lightsource_testresults.html')

    elif kind_of_test == 'weight':
        # load the template
        template = env.get_template('template_html/template_reward_weight_testresults.html')

    elif kind_of_test == 'range':
        # load the template
        template = env.get_template('template_html/template_EH_range_testresults.html')

    else:
        print("HTML file has FAILED to generate. No template for given kind of test")
        return

    # Render the template with the data
    rendered_html = template.render(data=results)
    with open(output_file, "w") as file:
        file.write(rendered_html)
    print("HTML file has been generated successfully.")
