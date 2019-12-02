import functools


def fuel_for_mass(mass):
    """
    Return calculated fuel by dividing mass by three, rounding down, and subtracting 2
    """
    return int(mass / 3) - 2


def sum_fuel(fuel_list):
    """
    Return accumulated sum of int values in fuel_list
    """
    return functools.reduce(lambda a, b: a+b, fuel_list)


def calc_total_fuel(mass):
    """
    Return final fuel for mass, including fuel required for the fuel mass itself
    """
    fuel = fuel_for_mass(mass)

    if fuel < 0:
        return 0

    added_fuel = calc_total_fuel(fuel)
    return fuel + added_fuel


if __name__ == '__main__':
    file_contents = open('input/mass.txt', 'r').read().splitlines()
    fuel_list = [fuel_for_mass(int(value)) for value in file_contents]
    result = sum_fuel(fuel_list)

    total_fuel_list = [calc_total_fuel(int(value)) for value in file_contents]
    improved_result = sum_fuel(total_fuel_list)

    print(result)
    print(improved_result)
