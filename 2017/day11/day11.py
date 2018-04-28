from collections import Counter
from common import input_utils as iu

def simplify(counter, list_dirs):
    assert len(list_dirs) == 2
    metric = min([counter[d] for d in list_dirs])
    for d in list_dirs:
        counter[d] -= metric


def compose(counter, list_dirs, res_dir):
    assert len(list_dirs) == 2
    metric = min([counter[d] for d in list_dirs])
    for d in list_dirs:
        counter[d] -= metric
    counter[res_dir] += metric


def resolve(c):
    simplify(c, ['n', 's'])
    simplify(c, ['ne', 'sw'])
    simplify(c, ['nw', 'se'])
    compose(c, ['se', 'sw'], 's')
    compose(c, ['ne', 'nw'], 'n')
    compose(c, ['n', 'se'], 'ne')
    compose(c, ['n', 'sw'], 'nw')
    compose(c, ['s', 'nw'], 'sw')
    compose(c, ['s', 'ne'], 'se')
    return c


def process_simple(inst):
    c = Counter(inst)
    resolve(c)
    return sum(c.values())


def process_furthest(inst):
    c = Counter()
    m = 0
    for i in range(len(inst)):
        c[inst[i]] += 1
        resolve(c)
        n = sum(c.values())
        if n > m:
            m = n
    return m


def run_test():
    assert process_simple(['ne', 'ne', 'ne']) == 3
    assert process_simple(['ne', 'ne', 'sw', 'sw']) == 0
    assert process_simple(['ne', 'ne', 's', 's']) == 2
    assert process_simple(['se', 'sw', 'se', 'sw', 'sw']) == 3


def main():
    run_test()
    inp = iu.get_input('input')
    inst = inp.split(',')
    print process_simple(inst)
    print process_furthest(inst)


if __name__ == '__main__':
    main()
