from collections import defaultdict


class Assembunny(object):
    def __init__(self, input_path):
        directions = open(input_path)
        rows = directions.readlines()
        self.instructions = [r.strip("\n") for r in rows]
        self.register = defaultdict(int)

    def copy(self, value, target):
        self.register[target] = self.register[value] if value in self.register else int(value)

    def inc(self, target):
        self.register[target] += 1

    def dec(self, target):
        self.register[target] -= 1

    def jnz(self, value, skip):
        try:
            int(value)
            return int(skip)
        except:
            return int(skip) if self.register[value] != 0 else 1

    def execute_instructions(self):
        i = 0
        while i < len(self.instructions):
            current_instruction = self.instructions[i]
            split_instruction = current_instruction.split(" ")
            if split_instruction[0] == "cpy":
                self.copy(split_instruction[1], split_instruction[2])
                i += 1
            elif split_instruction[0] == "inc":
                self.inc(split_instruction[1])
                i += 1
            elif split_instruction[0] == "dec":
                self.dec(split_instruction[1])
                i += 1
            elif split_instruction[0] == "jnz":
                i += self.jnz(split_instruction[1], split_instruction[2])


def run_test():
    a = Assembunny("test")
    a.execute_instructions()
    assert a.register['a'] == 42


def main():
    run_test()

    # part 1
    a = Assembunny("input")
    a.execute_instructions()
    print(a.register['a'])

    # part 2
    a = Assembunny("input")
    a.register['c'] = 1
    a.execute_instructions()
    print(a.register['a'])

if __name__ == '__main__':
    main()
