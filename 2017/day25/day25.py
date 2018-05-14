import sys
sys.path.append("../..")
from common import input_utils as iu
from collections import defaultdict


class Solution(object):
    def __init__(self, instructions):
        assert instructions[0].startswith('Begin')
        self.starting_state = instructions[0][-2]
        assert instructions[1].startswith('Perform')
        self.steps = int(instructions[1].split()[5])
        i = 0
        self.parsed_instructions = defaultdict(dict)
        while i < len(instructions):
            if instructions[i].startswith('In state'):
                state = instructions[i][-2]
            elif instructions[i].startswith('  If the current value'):
                current_value = int(instructions[i][-2])
            elif instructions[i].startswith('    - Write the value'):
                new_value = int(instructions[i][-2])
                self.parsed_instructions[state][current_value] = [new_value]
            elif instructions[i].startswith('    - Move one slot to the'):
                direction = 1 if instructions[i].split()[-1][:-1] == 'right' else -1
                self.parsed_instructions[state][current_value].append(direction)
            elif instructions[i].startswith('    - Continue with state'):
                new_state = instructions[i][-2]
                self.parsed_instructions[state][current_value].append(new_state)
            i += 1

    def run(self):
        tape = defaultdict(int)
        i = 0
        cursor = 0
        state = self.starting_state
        while i < self.steps:
            tape[cursor], direction, state = self.parsed_instructions[state][tape[cursor]]
            cursor += direction
            i += 1
        return sum(tape.values())


def run_test():
    inp = iu.get_multi_line_input('input_test')
    s = Solution(inp)
    assert s.run() == 3


def main():
    run_test()
    inp = iu.get_multi_line_input('input')
    s = Solution(inp)
    print s.run()

if __name__ == '__main__':
    main()
