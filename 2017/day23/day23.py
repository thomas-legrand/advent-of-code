import sys
sys.path.append("../..")
from common import input_utils as iu
from collections import defaultdict

SET = 'set'
SUB = 'sub'
MUL = 'mul'
JNZ = 'jnz'


class Solution(object):
    def __init__(self, instructions, initial_value_a):
        self.instructions = instructions
        self.register = defaultdict(int)
        self.register['a'] = initial_value_a

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

    def read2(self):
        h = 0
        b = 0
        c = 0
        if self.register['a'] != 0:
            b = 81 * 100 + 100000
            c = b + 17000
        while True:
            f = 1
            max_v = b
            for d in range(2, b):
                if b % d == 0:
                    f = 0
                if d > max_v:
                    break
                max_v = b / d
            if f == 0:
                h += 1
            if b == c:
                return h
            b += 17


def main():
    # run_test()
    inp = iu.get_multi_line_input('input')
    s = Solution(inp, 0)
    print s.read()
    s = Solution(inp, 1)
    print s.read2()

if __name__ == '__main__':
    main()
