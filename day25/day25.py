from collections import defaultdict


# TODO inherit from day12 Assembunny class
class AssembunnyTransmit(object):
    def __init__(self, input_path):
        directions = open(input_path)
        rows = directions.readlines()
        self.instructions = [r.strip("\n").split(" ") for r in rows]
        self.register = defaultdict(int)
        self.authorized_letters = ['a', 'b', 'c', 'd']
        self.last_transmission = -1

    def copy(self, value, target):
        try:
            int(target)
        except:
            self.register[target] = self.register[value] if value in self.register else int(value)

    def inc(self, target):
        self.register[target] += 1

    def dec(self, target):
        self.register[target] -= 1

    def jnz(self, value, skip):
        try:
            value = int(value)
        except:
            value = self.register[value]
        try:
            skip = int(skip)
        except:
            skip = self.register[skip]
        return skip if value != 0 else 1

    def tgl(self, i, value):
        try:
            away = int(value)
            target_i = i + away if away != 0 else 1
        except:
            target_i = i + self.register[value]
        if target_i not in range(len(self.instructions)):
            return
        inst = self.instructions[target_i]
        if len(inst) == 2:
            if inst[0] == "inc":
                inst[0] = "dec"
            else:
                inst[0] = "inc"
        if len(inst) == 3:
            if inst[0] == "jnz":
                inst[0] = "cpy"
            else:
                inst[0] = "jnz"

    def out(self, value):
        self.transmission_channel.add(value)

    def match_and_add(self, i, do):
        if i + 2 >= len(self.instructions):
            return False
        current = self.instructions[i]
        first_next = self.instructions[i + 1]
        second_next = self.instructions[i + 2]
        if not (current[0] == "inc" and first_next[0] == "dec" and second_next[0] == "jnz"):
            return False
        if not (first_next[1] == second_next[1] and second_next[2] == "-2" and current[1] in self.authorized_letters
                and first_next[1] in self.authorized_letters):
            return False
        if do:
            self.register[current[1]] += self.register[first_next[1]]
            self.register[first_next[1]] = 0
        return True

    def match_and_multiply(self, i):
        if i + 5 >= len(self.instructions):
            return False
        if not self.match_and_add(i + 1, False):
            return False
        current = self.instructions[i]
        first_next = self.instructions[i + 1]
        third_next = self.instructions[i + 3]
        fourth_next = self.instructions[i + 4]
        fifth_next = self.instructions[i + 5]
        # check instructions
        if not (current[0] == "cpy" and fourth_next[0] == "dec" and fifth_next[0] == "jnz"):
            return False
        # check variables
        if not (fourth_next[1] == fifth_next[1] and fifth_next[2] == "-5"):
            return False
        # this fixes the case where the sequence starts with "cpy 73 a"
        if current[1] not in self.register:
            try:
                value = int(current[1])
            except:
                value = self.register[current[1]]
        else:
            value = self.register[current[1]]
        self.register[first_next[1]] += value * self.register[fifth_next[1]]
        self.register[third_next[1]] = 0
        self.register[fifth_next[1]] = 0
        return True

    def execute_instructions(self):
        i = 0
        while i < len(self.instructions):
            current = self.instructions[i]
            if self.match_and_add(i, True):
                i += 3
            elif self.match_and_multiply(i):
                i += 6
            elif current[0] == "cpy":
                self.copy(current[1], current[2])
                i += 1
            elif current[0] == "inc":
                self.inc(current[1])
                i += 1
            elif current[0] == "dec":
                self.dec(current[1])
                i += 1
            elif current[0] == "jnz":
                i += self.jnz(current[1], current[2])
            elif current[0] == "tgl":
                self.tgl(i, current[1])
                i += 1
            elif current[0] == "out":
                value = self.register[current[1]]
                print(value)
                if self.last_transmission >= 0 and value != 1 - self.last_transmission:
                    return
                self.last_transmission = value
                i += 1


def main():
    transmission_channel = {}
    i = 0
    while transmission_channel != {0, 1}:
        print("i = " + str(i))
        a = AssembunnyTransmit("input")
        a.register['a'] = i
        a.execute_instructions()
        i += 1

if __name__ == '__main__':
    main()
