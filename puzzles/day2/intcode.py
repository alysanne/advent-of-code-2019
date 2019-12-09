def process_gravity_assist(values):
    for i in range(0, len(values), 4):
        op_code = values[i]

        if op_code == 99:
            break

        # Get positions for operations
        try:
            position1 = values[i+1]
            position2 = values[i+2]
            position3 = values[i+3]
        except IndexError:
            raise Exception('Could not access position for operation')

        if op_code == 1:
            values[position3] = values[position1] + values[position2]
        elif op_code == 2:
            values[position3] = values[position1] * values[position2]
        else:
            raise Exception('Oops! That\'s not a valid opcode!')

    return values


def find_initial_inputs(instructions, expected_output):
    print('Finding values...')

    for i in range(0, 100):
        for j in range(0, 100):
            list_instr = _create_list(instructions)
            values = _init_memory(i, j, list_instr)
            result = process_gravity_assist(values)

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

    result = process_gravity_assist(values)
    print('Output: {}'.format(result[0]))

    # Find inputs for output 19690720
    inputs = find_initial_inputs(file_contents, 19690720)
    print(inputs)
