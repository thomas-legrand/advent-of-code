def get_input(input_path):
    directions = open(input_path)
    rows = directions.readlines()
    return [r.strip("\n") for r in rows]


def run_test():
    register = {}
    instructions = get_input("test")
    execute_instructions(instructions, register)
    assert register['a'] == 42


def execute_instructions(instructions, register):
    i = 0
    while i < len(instructions):
        current_instruction = instructions[i]
        split_instruction = current_instruction.split(" ")
        if split_instruction[0] == "cpy":
            if split_instruction[1] in register:
                register[split_instruction[2]] = register[split_instruction[1]]
            else:
                register[split_instruction[2]] = int(split_instruction[1])
            i += 1
        elif split_instruction[0] == "inc":
            if split_instruction[1] not in register:
                register[split_instruction[1]] = 1
            else:
                register[split_instruction[1]] += 1
            i += 1
        elif split_instruction[0] == "dec":
            if split_instruction[1] not in register:
                register[split_instruction[1]] = -1
            else:
                register[split_instruction[1]] -= 1
            i += 1
        elif split_instruction[0] == "jnz":
            if split_instruction[1] in register and register[split_instruction[1]] != 0:
                i += int(split_instruction[2])
            else:
                try:
                    int(split_instruction[1])
                    i += int(split_instruction[2])
                except Exception as e:
                    register[split_instruction[1]] = 0
                    i += 1


def main():
    run_test()
    instructions = get_input("input")

    # part 1
    register = {}
    execute_instructions(instructions, register)
    print(register['a'])

    # part 2
    register = {'c': 1}
    execute_instructions(instructions, register)
    print(register['a'])


if __name__ == '__main__':
    main()
