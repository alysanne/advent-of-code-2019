def find_closest_intersection(cable1, cable2):
    cable1_coordinates = get_coordinates_set(cable1)
    cable2_coordinates = get_coordinates_set(cable2)

    matches = cable1_coordinates.intersection(cable2_coordinates)

    return min([_calc_manhattan_dist(match) for match in matches])


def _calc_manhattan_dist(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1])


def get_coordinates_set(cable):
    cable_coordinates = set()
    cable_list = cable.split(',')

    position = {'x': 0, 'y': 0}  # Cable position as (x, y)

    for move in cable_list:
        for i in range(int(move[1:])):
            if move[0] == 'U':
                position['y'] += 1
            elif move[0] == 'D':
                position['y'] -= 1
            elif move[0] == 'R':
                position['x'] += 1
            elif move[0] == 'L':
                position['x'] -= 1

            cable_coordinates.add((position['x'], position['y']))

    return cable_coordinates


if __name__ == '__main__':
    file_contents = open('input/cables.txt', 'r').readlines()
    result = find_closest_intersection(*file_contents)

    print(result)
