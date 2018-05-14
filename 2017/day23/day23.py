import sys
sys.path.append("../..")
from common import input_utils as iu
from collections import defaultdict

SET = 'set'
SUB = 'sub'
MUL = 'mul'
JNZ = 'jnz'


class Solution(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.register = defaultdict(int)

    def read(self):
        def calc(v):
            try:
                return int(v)
            except ValueError:
                return self.register[v]
        count_mul = 0
        i = 0
        while 0 <= i < len(self.instructions):
            tokens = self.instructions[i].split()
            if tokens[0] == SET:
                self.register[tokens[1]] = calc(tokens[2])
            elif tokens[0] == SUB:
                self.register[tokens[1]] -= calc(tokens[2])
            elif tokens[0] == MUL:
                self.register[tokens[1]] *= calc(tokens[2])
                count_mul += 1
            elif tokens[0] == JNZ and calc(tokens[1]) != 0:
                i += calc(tokens[2])
                continue
            i += 1
        return count_mul


def main():
    # run_test()
    inp = iu.get_multi_line_input('input')
    s = Solution(inp)
    print s.read()

if __name__ == '__main__':
    main()
