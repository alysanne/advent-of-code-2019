def calc_possible_passwords(start, end):
    count = 0

    for n in range(int(start), int(end) + 1):
        valid = check_if_valid(str(n))

        if valid:
            count += 1

    return count


def check_if_valid(password):
    digit_count = {}
    prev_digit = 0

    for digit in password:
        _count_equals(digit, digit_count)
        if not _digits_increase(digit, prev_digit):
            return False

        prev_digit = int(digit)

    if 2 in digit_count.values():
        return True
    return False


def _count_equals(digit, digit_count):
    # Rules:
    # Two adjacent digits are the same (like 22 in 122345).
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1


def _digits_increase(digit, prev_digit):
    # Rules:
    # From left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    if prev_digit > int(digit):
        return False
    return True


if __name__ == "__main__":
    file_contents = open('input/range.txt', 'r').read().split('-')
    num_pwds = calc_possible_passwords(*file_contents)
    print("There are {} valid passwords in the range".format(num_pwds))
