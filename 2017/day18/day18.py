from common import input_utils as iu
from collections import defaultdict

SET = 'set'
ADD = 'add'
MUL = 'mul'
MOD = 'mod'
SND = 'snd'
RCV = 'rcv'
JGZ = 'jgz'


class Solution(object):
    def __init__(self, instructions, program_id):
        self.instructions = instructions
        self.register = defaultdict(int)
        self.register['p'] = program_id
        self.input_queue = []
        self.output_queue = []
        self.progress = 0
        self.values_sent = 0
        self.values_received = 0

    def read(self):
        def calc(v):
            try:
                return int(v)
            except ValueError as e:
                return self.register[v]

        i = 0
        last_played = 0
        while 0 <= i < len(self.instructions):
            tokens = self.instructions[i].split()
            if tokens[0] == SET:
                self.register[tokens[1]] = calc(tokens[2])
            elif tokens[0] == ADD:
                self.register[tokens[1]] += calc(tokens[2])
            elif tokens[0] == MUL:
                self.register[tokens[1]] *= calc(tokens[2])
            elif tokens[0] == MOD:
                self.register[tokens[1]] = self.register[tokens[1]] % calc(tokens[2])
            elif tokens[0] == SND:
                last_played = self.register[tokens[1]]
            elif tokens[0] == RCV:
                if calc(tokens[1]) != 0:
                    return last_played
            elif tokens[0] == JGZ:
                i = i + calc(tokens[2]) if self.register[tokens[1]] > 0 else i + 1
                continue
            i += 1

    def send_to(self, program):
        program.input_queue += self.output_queue
        self.output_queue = []

    def read_2(self):
        def calc(v):
            try:
                return int(v)
            except ValueError:
                return self.register[v]

        while self.progress < len(self.instructions):
            # print 'program {} progressed until {}'.format(self.program_id, self.progress)
            tokens = self.instructions[self.progress].split()
            if tokens[0] == SET:
                self.register[tokens[1]] = calc(tokens[2])
            elif tokens[0] == ADD:
                self.register[tokens[1]] += calc(tokens[2])
            elif tokens[0] == MUL:
                self.register[tokens[1]] *= calc(tokens[2])
            elif tokens[0] == MOD:
                self.register[tokens[1]] = self.register[tokens[1]] % calc(tokens[2])
            elif tokens[0] == SND:
                self.output_queue.append(calc(tokens[1]))
                self.values_sent += 1
            elif tokens[0] == RCV:
                if self.input_queue:
                    self.register[tokens[1]] = self.input_queue.pop(0)
                    self.values_received += 1
                else:
                    return
            elif tokens[0] == JGZ:
                self.progress += calc(tokens[2]) if calc(tokens[1]) > 0 else 1
                continue
            self.progress += 1


# unused
class DecompiledSolution(object):
    def __init__(self):
        self.input_queue = []
        self.output_queue = []
        self.values_sent = 0
        self.values_received = 0

    def read(self):
        a = 2 ** 31 - 1
        p = 735
        for _ in range(127):
            p = (((p * 8505) % a) * 129749 + 12345) % a
            b = p % 10000
            self.output_queue.append(b)
        while True:
            while True:
                f = 0
                if self.input_queue:
                    a = self.input_queue.pop(0)
                else:
                    return
                for _ in range(126):
                    if self.input_queue:
                        b = self.input_queue.pop(0)
                    else:
                        return
                    if b <= a:
                        self.output_queue.append(a)
                        a = b
                    else:
                        self.output_queue.append(b)
                        f = 1
                self.output_queue.append(a)
                if f <= 0:
                    break
            if a <= 0:
                break
            while True:
                if self.input_queue:
                    b = self.input_queue.pop(0)
                else:
                    return
                if b <= 0:
                    break


def run_duet(instructions):
    s0 = Solution(instructions, 0)
    s1 = Solution(instructions, 1)
    l = 0
    while True:
        s0.read_2()
        s0.send_to(s1)
        s1.read_2()
        s1.send_to(s0)
        if s0.input_queue:
            l += len(s0.input_queue)
        if not s0.input_queue:
            break
    return s1.values_sent


def run_test():
    inp = iu.get_multi_line_input('test_input')
    s = Solution(inp, 0)
    assert s.read() == 4
    inp2 = iu.get_multi_line_input('test_input_2')
    assert run_duet(inp2) == 3


def main():
    run_test()
    inp = iu.get_multi_line_input('input')
    s = Solution(inp, 0)
    print s.read()
    print run_duet(inp)

if __name__ == '__main__':
    main()
