import itertools

from day5.air_conditioner import process_intcode


def calc_thruster_signal(sequence, controller_program):
    signal = 0

    for phase in sequence:
        program = controller_program[:]
        inputs = [phase, signal]
        outputs = process_intcode(program, inputs)
        signal = outputs.pop()

    return signal


if __name__ == '__main__':
    file_contents = open('input/controller_software.txt', 'r').read().split(',')
    values = list(map(lambda x: int(x), file_contents))

    sequences = itertools.permutations([0, 1, 2, 3, 4])
    results = [calc_thruster_signal(sequence, values) for sequence in sequences]

    max_output = max(results)
    print("Max signal is {}".format(max_output))
