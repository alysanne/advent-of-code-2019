def checksum_orbits(orbit_list):
    orbit_map = _create_orbit_map(orbit_list)
    result = 0

    for k in orbit_map:
        result += 1 + _get_orbits(orbit_map[k], orbit_map)

    return result


def calculate_distance(orbit_list):
    orbit_map = _create_orbit_map(orbit_list)
    you_path = _path_to('YOU', orbit_map)
    santa_path = _path_to('SAN', orbit_map)

    # Remove YOU and SAN from calculations
    you_path.remove('YOU')
    santa_path.remove('SAN')

    you_diff = you_path.difference(santa_path)
    santa_diff = santa_path.difference(you_path)

    return len(you_diff) + len(santa_diff)


def _create_orbit_map(orbit_list):
    orbits = {}
    for orbit in orbit_list:
        objects = orbit.split(')')
        orbits[objects[1]] = objects[0]
    return orbits


def _get_orbits(obj, orbit_map):
    if obj in orbit_map:
        return 1 + _get_orbits(orbit_map[obj], orbit_map)
    return 0


def _path_to(obj, orbit_map):
    if obj in orbit_map:
        path_to = _path_to(orbit_map[obj], orbit_map)
        path_to.add(obj)
        return path_to
    else:
        return set()


if __name__ == '__main__':
    file_contents = open('input/map_data.txt').read().splitlines()

    result = checksum_orbits(file_contents)
    print("Number of orbits: {}".format(result))

    result2 = calculate_distance(file_contents)
    print("Distance to santa: {}".format(result2))
