def calc_possible_passwords(start, end):
    count = 0

    for n in range(int(start), int(end) + 1):
        valid = check_if_valid(n)

        if valid:
            count += 1

    return count


def check_if_valid(password):
    str_pwd = str(password)
    rules = {'equals': False, 'increase': True}
    for k in range(len(str_pwd) - 1):
        rules['equals'] = rules['equals'] or _check_equals(str_pwd[k], str_pwd[k+1])
        rules['increase'] = rules['increase'] and _check_increase(str_pwd[k], str_pwd[k + 1])

    if not rules['equals'] or not rules['increase']:
        return False
    return True


def _check_equals(a, b):
    # Rules:
    # Two adjacent digits are the same (like 22 in 122345).
    if a == b:
        return True
    return False


def _check_increase(a, b):
    # Rules:
    # From left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    if int(a) <= int(b):
        return True
    return False


if __name__ == "__main__":
    file_contents = open('input/range.txt', 'r').read().split('-')
    num_pwds = calc_possible_passwords(*file_contents)
    print("There are {} valid passwords in the range".format(num_pwds))
