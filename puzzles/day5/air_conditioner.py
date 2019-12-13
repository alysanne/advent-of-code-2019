from day2.intcode import handle_math_ops, get_value_for_mode


def process_intcode(values, input_programme):
    i = 0
    step = 0
    while i < len(values):
        op_code = values[i] % 100
        modes = str(values[i])[:-2]

        if op_code == 99:
            break

        # op_code 1: add
        # op_code 2: multiply
        if op_code in [1, 2]:
            handle_math_ops(i, op_code, values, modes)
            step = 4

        # op_code 3: input
        if op_code == 3:
            position = values[i+1]
            values[position] = input_programme
            step = 2

        # op_code 4: output
        if op_code == 4:
            value = get_value_for_mode(i, 1, modes, values)
            print(value)
            step = 2

        # Skip to next instruction
        i += step

    return values


if __name__ == '__main__':
    file_contents = open('input/diagnostic.txt', 'r').read().split(',')
    values = list(map(lambda x: int(x), file_contents))

    print("First run...")
    process_intcode(values, 1)

    print("Second run...")
    process_intcode(values, 5)
