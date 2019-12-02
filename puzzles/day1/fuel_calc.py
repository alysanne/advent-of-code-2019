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


if __name__ == '__main__':
    file_contents = open('input/mass.txt', 'r').read().splitlines()
    fuel_list = [fuel_for_mass(int(value)) for value in file_contents]
    result = sum_fuel(fuel_list)

    print(result)
