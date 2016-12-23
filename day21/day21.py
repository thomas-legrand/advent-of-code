import re
from itertools import permutations


def get_input(input_path):
    directions = open(input_path)
    rows = directions.readlines()
    return [r.strip("\n") for r in rows]


class EncryptPassword(object):
    def __init__(self, initial_pass):
        self.initial_pass = initial_pass
        self.scrambled_pass = list(initial_pass)

    def swap_position(self, positions):
        assert len(positions) == 2
        self.scrambled_pass[positions[0]], self.scrambled_pass[positions[1]] = \
            self.scrambled_pass[positions[1]], self.scrambled_pass[positions[0]]

    def swap_letters(self, letters):
        assert len(letters) == 2
        for i, letter in enumerate(self.scrambled_pass):
            if letter == letters[0]:
                self.scrambled_pass[i] = letters[1]
            elif letter == letters[1]:
                self.scrambled_pass[i] = letters[0]

    def rotate_left(self, num_steps):
        n = len(self.scrambled_pass)
        self.scrambled_pass = self.scrambled_pass[(num_steps % n):] + self.scrambled_pass[:(num_steps % n)]

    def rotate_right(self, num_steps):
        self.rotate_left(-num_steps)

    def reverse(self, positions):
        assert len(positions) == 2
        self.scrambled_pass[positions[0]:(positions[1] + 1)] = self.scrambled_pass[positions[0]:(positions[1] + 1)][::-1]

    def move(self, positions):
        assert len(positions) == 2
        l = self.scrambled_pass[positions[0]]
        del self.scrambled_pass[positions[0]]
        self.scrambled_pass = self.scrambled_pass[:positions[1]] + [l] + self.scrambled_pass[positions[1]:]

    def apply_instruction(self, instruction):
        letters = re.findall("""\s(\w)(?:$|\s)""", instruction)
        numbers = [int(s) for s in re.findall("""\d+""", instruction)]
        if instruction.startswith("swap position"):
            self.swap_position(numbers)
        elif instruction.startswith("swap letter"):
            self.swap_letters(letters)
        elif instruction.startswith("rotate"):
            if "left" in instruction:
                self.rotate_left(numbers[0])
            elif "right" in instruction:
                self.rotate_right(numbers[0])
            elif "based" in instruction:
                i = self.scrambled_pass.index(letters[0])
                num_steps = 1 + i
                if i >= 4:
                    num_steps += 1
                self.rotate_right(num_steps)
        elif instruction.startswith("reverse"):
            self.reverse(numbers)
        elif instruction.startswith("move"):
            self.move(numbers)

    def scramble(self, instructions):
        for instruction in instructions:
            self.apply_instruction(instruction)




def run_tests():
    instructions = get_input("test")
    password = EncryptPassword("abcde")
    for instruction in instructions:
        password.apply_instruction(instruction)
    assert "".join(password.scrambled_pass) == "decab"


def main():
    run_tests()
    instructions = get_input("input")
    password = EncryptPassword("abcdefgh")
    password.scramble(instructions)
    print("".join(password.scrambled_pass))

    for p in permutations("abcdefgh"):
        password = EncryptPassword("".join(p))
        password.scramble(instructions)
        if "".join(password.scrambled_pass) == "fbgdceah":
            print("".join(p))
            break


if __name__ == '__main__':
    main()