import os

KEYPAD = [range(i * 3 + 1, (i + 1) * 3 + 1) for i in range(3)]
MOVES = {
    "U": lambda s: s.move_up(),
    "D": lambda s: s.move_down(),
    "L": lambda s: s.move_left(),
    "R": lambda s: s.move_right()
}


def get_input(input_path):
    directions = open(input_path)
    instructions_string = directions.readlines()
    return [instruction.rstrip("\n") for instruction in instructions_string]


class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        if self.y > 0:
            self.y -= 1

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self):
        if self.x < 2:
            self.x += 1

    def move_down(self):
        if self.y < 2:
            self.y += 1


def main():
    input_path = os.path.join('input', 'directions')
    print get_input(input_path)
    print [range(i * 3 + 1, (i + 1) * 3 + 1) for i in range(3)]
    input = get_input(input_path)
    for input_line in input:
        s = State(0, 0)
        [MOVES[instruction](s) for instruction in input_line]
        print s.x, s.y
        print KEYPAD[s.y][s.x]


if __name__ == '__main__':
    main()
