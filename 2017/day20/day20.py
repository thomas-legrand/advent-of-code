import re
from collections import Counter


def get_multi_line_input(f_name):
    f = open(f_name)
    return f.read().splitlines()


class Particle(object):
    def __init__(self, x, v, a):
        self.x = x
        self.v = v
        self.a = a

    def get_distance(self, t):
        position = self.get_position(t)
        return sum(map(abs, position))

    def get_position(self, t):
        sum_t = sum(range(t + 1))
        return [self.x[i] + t * self.v[i] + sum_t * self.a[i] for i in range(3)]


def parse_particle(l):
    return map(lambda s: map(int, s.split(',')), re.findall(r'<([0-9,-]+)>', l))


def find_closest(inp, t):
    particles = [Particle(*parse_particle(i)) for i in inp]
    distances = map(lambda p: Particle.get_distance(p, t), particles)
    return distances.index(min(distances))


def resolve_collisions(inp, final_t):
    particles = [Particle(*parse_particle(i)) for i in inp]
    for t in range(final_t):
        positions = map(lambda p: tuple(p.get_position(t)), particles)
        position_counts = Counter(positions)
        duplicate_positions = [p for p in position_counts if position_counts[p] > 1]
        particles = [p for p in particles if tuple(p.get_position(t)) not in duplicate_positions]
    return len(particles)


def run_test():
    inp = get_multi_line_input('test_input')
    assert find_closest(inp, 100) == 0
    inp = get_multi_line_input('test_input_2')
    assert resolve_collisions(inp, 100) == 1


def main():
    run_test()
    inp = get_multi_line_input('input')
    print find_closest(inp, 1000)
    print resolve_collisions(inp, 1000)


if __name__ == '__main__':
    main()
