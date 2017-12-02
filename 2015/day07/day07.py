
registry = {'b': 46065}
instructions = []

def get_multi_line_input(f_name):
    f = open(f_name)
    return f.read().splitlines()

def process():
    global registry, instructions
    instruction = instructions.pop(0)
    words = instruction.split(' ')
    if 'AND' in instruction:
        if words[2] in registry:
            try:
                registry[words[-1]] = int(words[0]) & registry[words[2]]
            except ValueError as e:
                if words[0] not in registry:
                    instructions.append(instruction)
                else:
                    if not words[-1] == 'b':
                        registry[words[-1]] = registry[words[0]] & registry[words[2]]
        else:
            instructions.append(instruction)
    elif 'OR' in instruction:
        if words[0] not in registry or words[2] not in registry:
            instructions.append(instruction)
        else:
            if not words[-1] == 'b':
                registry[words[-1]] = registry[words[0]] | registry[words[2]]
    elif 'NOT' in instruction:
        if words[1] not in registry:
            instructions.append(instruction)
        else:
            if not words[-1] == 'b':
                registry[words[-1]] = ~registry[words[1]] & 0xffff
    elif 'LSHIFT' in instruction:
        if words[0] not in registry:
            instructions.append(instruction)
        else:
            if not words[-1] == 'b':
                registry[words[-1]] = registry[words[0]] << int(words[2])
    elif 'RSHIFT' in instruction:
        if words[0] not in registry:
            instructions.append(instruction)
        else:
            if not words[-1] == 'b':
                registry[words[-1]] = registry[words[0]] >> int(words[2])
    else:
        try:
            if not words[-1] == 'b':
                registry[words[-1]] = int(words[0])
        except ValueError as e:
            if words[0] not in registry:
                instructions.append(instruction)
            else:
                if not words[-1] == 'b':
                    registry[words[-1]] = registry[words[0]]




def run_test():
    global instructions
    instructions = get_multi_line_input('input_test')
    while len(instructions) > 0:
        process()
    assert registry['d'] == 72



def main():
    global instructions
    # run_test()
    instructions = get_multi_line_input('input')
    while len(instructions) > 0:
        process()
    print registry['a']


if __name__ == '__main__':
    main()