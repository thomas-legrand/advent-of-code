import os
import re
import numpy as np

POSSIBLE_DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
POSSIBLE_TURNS = {"R": -np.pi / 2, "L": np.pi / 2}


class Instruction(object):
    def __init__(self, turn, number):
        assert turn in POSSIBLE_TURNS
        self.turn = turn
        self.number = number

    def __str__(self):
        return "direction %(d)s - number %(n)s" % {'d': self.turn, 'n': self.number}


class State(object):
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __str__(self):
        return "position %(p)s - direction %(d)s" % {'p': self.position, 'd': self.direction}

    def move(self, instruction):
        assert isinstance(instruction, Instruction)
        # first update the direction
        angle = POSSIBLE_TURNS[instruction.turn]
        updated_direction_list = get_new_direction(self.direction, angle)
        self.direction = updated_direction_list

        # then update the position
        assert self.direction in POSSIBLE_DIRECTIONS
        change = [d * instruction.number for d in self.direction]
        self.position = [sum(x) for x in zip(self.position, change)]


def get_new_direction(direction, angle):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    np_direction = np.array(direction)
    updated_direction = np.dot(rotation_matrix, np_direction).astype(int)
    return updated_direction.tolist()


def get_instruction_from_string(s):
    d = re.search(r"[A-Z]", s)
    n = re.search(r"\d+", s)
    return Instruction(d.group(0), int(n.group(0)))


def fetch_input_list_instructions(input_path):
    directions = open(input_path)
    instructions_string = directions.read()
    return [get_instruction_from_string(s) for s in instructions_string.split(", ")]


def main():
    input_path = os.path.join('input', 'directions')
    instructions = fetch_input_list_instructions(input_path)
    # start with initial state (x = 0, y = 0) in a 2D plane, and head towards increasing x.
    a = State([0, 0], [1, 0])
    print a
    for i in instructions:
        print i
        a.move(i)
        print a
    print sum(map(abs, a.position))


if __name__ == '__main__':
    main()
