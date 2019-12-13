def process_intcode(values):
    i = 0
    while i < len(values):
        op_code = values[i]

        if op_code == 99:
            break

        handle_math_ops(i, op_code, values)

        # Skip to next instruction
        i += 4

    return values


def handle_math_ops(i, op_code, values, modes=''):
    op_values = {}
    # Get values for operations
    try:
        for position in range(1, 3):
            op_values['value' + str(position)] = get_value_for_mode(i, position, modes, values)
    except IndexError:
        raise Exception('Could not access value for operation')

    if op_code == 1:
        values[values[i+3]] = op_values['value1'] + op_values['value2']
    elif op_code == 2:
        values[values[i+3]] = op_values['value1'] * op_values['value2']


def get_value_for_mode(i, position, modes, values):
    try:
        mode = modes[-position]
    except:
        mode = '0'

    if mode == '1':
        value = values[i + position]
    else:
        value = values[values[i + position]]
    return value


def find_initial_inputs(instructions, expected_output):
    print('Finding values...')

    for i in range(0, 100):
        for j in range(0, 100):
            list_instr = _create_list(instructions)
            values = _init_memory(i, j, list_instr)
            result = process_intcode(values)

            if result[0] == expected_output:
                return 'Found!: noun {}, verb {}'.format(i, j)

    raise Exception('Initial inputs not found :(')


def _init_memory(noun, verb, list_instr):
    list_instr[1] = noun
    list_instr[2] = verb
    return list_instr


def _create_list(values):
    return list(map(lambda a: int(a), values.split(',')))


if __name__ == '__main__':
    file_contents = open('input/gravity_assist.txt', 'r').read()
    values = list(map(lambda a: int(a), file_contents.split(",")))

    # Initial replacements for 1202 program alarm
    values[1] = 12
    values[2] = 2

    result = process_intcode(values)
    print('Output: {}'.format(result[0]))

    # Find inputs for output 19690720
    inputs = find_initial_inputs(file_contents, 19690720)
    print(inputs)
