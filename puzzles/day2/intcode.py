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


if __name__ == '__main__':
    file_contents = open('input/gravity_assist.txt', 'r').read()
    values = list(map(lambda a: int(a), file_contents.split(",")))

    # Initial replacements for 1202 program alarm
    values[1] = 12
    values[2] = 2

    result = process_gravity_assist(values)

    print(result)
