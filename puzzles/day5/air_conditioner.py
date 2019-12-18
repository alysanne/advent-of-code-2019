from day2.intcode import handle_math_ops, get_value_for_mode


def process_intcode(values, inputs):
    i = 0
    step = 0
    outputs = []

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
            input_value = inputs.pop(0) if isinstance(inputs, list) else inputs
            position = values[i+1]
            values[position] = input_value
            step = 2

        # op_code 4: output
        if op_code == 4:
            value = get_value_for_mode(i, 1, modes, values)
            print(value)
            outputs.append(value)
            step = 2

        # op_code 5: jump if non-zero
        # op_code 6: jump if zero
        if op_code in [5, 6]:
            jump_to = handle_jump_ops(i, op_code, modes, values)
            i = jump_to
            continue

        # op_code 7: less than
        # op_code 8: equals
        if op_code in [7, 8]:
            handle_comparison_ops(i, op_code, modes, values)
            step = 4

        # Skip to next instruction
        i += step

    return outputs


def handle_jump_ops(i, op_code, modes, values):
    parameters = {}
    for position in range(1, 3):
        parameters['parameter' + str(position)] = get_value_for_mode(i, position, modes, values)

    if op_code == 5:
        if parameters['parameter1'] != 0:
            jump_to = parameters['parameter2']
        else:
            jump_to = i + 3

    if op_code == 6:
        if parameters['parameter1'] == 0:
            jump_to = parameters['parameter2']
        else:
            jump_to = i + 3

    return jump_to


def handle_comparison_ops(i, op_code, modes, values):
    parameters = {}
    for position in range(1, 3):
        parameters['parameter' + str(position)] = get_value_for_mode(i, position, modes, values)

    if op_code == 7:
        if parameters['parameter1'] < parameters['parameter2']:
            values[values[i + 3]] = 1
        else:
            values[values[i + 3]] = 0

    if op_code == 8:
        if parameters['parameter1'] == parameters['parameter2']:
            values[values[i + 3]] = 1
        else:
            values[values[i + 3]] = 0


if __name__ == '__main__':
    file_contents = open('input/diagnostic.txt', 'r').read().split(',')

    print("First run...")
    values = list(map(lambda x: int(x), file_contents))
    process_intcode(values, 1)

    print("Second run...")
    values2 = list(map(lambda x: int(x), file_contents))
    process_intcode(values2, 5)
