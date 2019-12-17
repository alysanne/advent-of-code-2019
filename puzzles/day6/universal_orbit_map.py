def checksum_orbits(orbit_list):
    orbit_map = _create_orbit_map(orbit_list)
    result = 0

    for k in orbit_map:
        result += 1 + _get_orbits(orbit_map[k], orbit_map)

    return result


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


if __name__ == '__main__':
    file_contents = open('input/map_data.txt').read().splitlines()

    result = checksum_orbits(file_contents)
    print("Number of orbits: {}".format(result))
