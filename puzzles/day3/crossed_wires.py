def find_closest_intersection(cable1, cable2):
    cable1_coordinates, _ = get_coordinates(cable1)
    cable2_coordinates, _ = get_coordinates(cable2)

    matches = cable1_coordinates.intersection(cable2_coordinates)

    return min([_calc_manhattan_dist(match) for match in matches])


def _calc_manhattan_dist(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1])


def get_coordinates(cable):
    cable_coordinates = set()
    steps_for_coordinates = {}
    cable_list = cable.split(',')
    step_count = 0

    position = {'x': 0, 'y': 0}  # Cable position as (x, y)

    for move in cable_list:
        for i in range(int(move[1:])):
            step_count += 1

            if move[0] == 'U':
                position['y'] += 1
            elif move[0] == 'D':
                position['y'] -= 1
            elif move[0] == 'R':
                position['x'] += 1
            elif move[0] == 'L':
                position['x'] -= 1

            coordinates = (position['x'], position['y'])
            cable_coordinates.add(coordinates)
            if coordinates not in steps_for_coordinates:
                steps_for_coordinates[coordinates] = step_count

    return cable_coordinates, steps_for_coordinates


def find_min_intersection(cable1, cable2):
    cable1_coordinates, cable1_steps = get_coordinates(cable1)
    cable2_coordinates, cable2_steps = get_coordinates(cable2)

    matches = cable1_coordinates.intersection(cable2_coordinates)

    return min([cable1_steps[match] + cable2_steps[match] for match in matches])


if __name__ == '__main__':
    file_contents = open('input/cables.txt', 'r').readlines()
    result = find_closest_intersection(*file_contents)

    print('Closest intersection distance: {}'.format(result))

    min_steps = find_min_intersection(*file_contents)

    print('Min intersection steps: {}'.format(min_steps))
