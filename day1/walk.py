import os
import re
import copy
import numpy as np

# note: a pretty cool solution exists, using complex numbers, at
# https://dannythecoder.wordpress.com/2016/12/02/walking-paths-with-complex-numbers/

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

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def move_one_block(self):
        self.position = [sum(x) for x in zip(self.position, self.direction)]

    def move(self, instruction):
        assert isinstance(instruction, Instruction)
        # first update the direction
        angle = POSSIBLE_TURNS[instruction.turn]
        updated_direction_list = get_new_direction(self.direction, angle)
        assert updated_direction_list in POSSIBLE_DIRECTIONS
        self.direction = updated_direction_list
        inter_positions = []

        for i in xrange(instruction.number):
            self.move_one_block()
            inter_positions.append(self.position)

        return inter_positions


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


def compute_position_sequence_from_instructions(initial_state, instructions):
    visited_positions = [initial_state.position]
    current_state = copy.copy(initial_state)
    for instruction in instructions:
        new_positions = current_state.move(instruction)
        visited_positions += new_positions
    return visited_positions


def compute_position_visited_twice(visited_positions):
    for i, position in enumerate(visited_positions):
        if position in visited_positions[:i]:
            return position


def main():
    input_path = os.path.join('input', 'directions')
    instructions = fetch_input_list_instructions(input_path)
    # start with initial state (x = 0, y = 0) in a 2D plane, and head towards increasing x.
    initial_state = State([0, 0], [1, 0])
    visited_position = compute_position_sequence_from_instructions(initial_state, instructions)
    print(sum(map(abs, visited_position[-1])))
    first_visited_twice = compute_position_visited_twice(visited_position)
    print(sum(map(abs, first_visited_twice)))


if __name__ == '__main__':
    main()
