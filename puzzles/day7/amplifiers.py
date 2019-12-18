import itertools

from day2.intcode import handle_math_ops, get_value_for_mode
from day5.air_conditioner import process_intcode, handle_jump_ops, handle_comparison_ops


def calc_thruster_signal(sequence, controller_program):
    signal = 0

    for phase in sequence:
        program = controller_program[:]
        inputs = [phase, signal]
        outputs = process_intcode(program, inputs)
        signal = outputs.pop()

    return signal


def feedback_loop(sequence, controller_program):
    instruction = {
        'instruction1': controller_program[:],
        'instruction2': controller_program[:],
        'instruction3': controller_program[:],
        'instruction4': controller_program[:],
        'instruction5': controller_program[:]
    }
    pointers = {}
    inputs = [0]
    last_output = 0
    counter = 0

    for phase in sequence:
        counter += 1
        pointers['index' + str(counter)], output = process_intcode_loop(instruction['instruction' + str(counter)],
                                                                        [phase, inputs.pop()])
        inputs.append(output)

    counter = 0
    while instruction['instruction1'][pointers['index5']] != 99:
        counter += 1

        pointers['index' + str(counter)], output = process_intcode_loop(instruction['instruction' + str(counter)],
                                                                        inputs.pop(),
                                                                        i=pointers['index' + str(counter)])
        inputs.append(output)

        if output == 'end':
            continue

        if counter == 5:
            last_output = output
            counter = 0

    return last_output


def process_intcode_loop(values, inputs, i=0):
    step = 0

    while i < len(values):
        op_code = values[i] % 100
        modes = str(values[i])[:-2]

        if op_code == 99:
            return i, 'end'

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
            return i+2, value

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


if __name__ == '__main__':
    file_contents = open('input/controller_software.txt', 'r').read().split(',')
    values = list(map(lambda x: int(x), file_contents))

    sequences = itertools.permutations([0, 1, 2, 3, 4])
    results = [calc_thruster_signal(sequence, values) for sequence in sequences]

    max_output = max(results)
    print("Max signal is {}".format(max_output))

    sequences = itertools.permutations([5, 6, 7, 8, 9])
    results = [feedback_loop(sequence, values) for sequence in sequences]

    max_output = max(results)
    print("Max signal with feedback loop is {}".format(max_output))
