from collections import Counter


balancing_weight = None


def get_multi_line_input(f_name):
    f = open(f_name)
    return f.read().splitlines()


def bottom(inp):
    m = set()
    n = set()
    x = [i.split(' -> ') for i in inp]
    for i in x:
        m.add(i[0].split()[0])
        if len(i) > 1:
            for j in i[1].split(', '):
                n.add(j)
    for e in n:
        m.remove(e)
    return m.pop()


def parse(inp):
    initial_weights = {}
    supported_nodes = {}
    x = [i.split(' -> ') for i in inp]
    for item in x:
        bottom_program, bottom_program_weight = item[0].split()
        initial_weights[bottom_program] = int(bottom_program_weight[1:-1])
        if len(item) > 1:
            supported_nodes[bottom_program] = item[1].split(', ')
    return supported_nodes, initial_weights


def compute_total_weight(supported_nodes, initial_weights):
    final_weights = {}
    for program in initial_weights:
        if program not in supported_nodes:
            # assign final weights to root
            final_weights[program] = initial_weights[program]

    def get_program_final_weight(program):
        global balancing_weight
        if program in final_weights:
            return final_weights[program]
        else:
            supported_weights = [get_program_final_weight(p) for p in supported_nodes[program]]
            if None in supported_weights:
                # return early if balancing weight is one of the supported weights
                return None
            unique_weights = set(supported_weights)
            if len(unique_weights) > 1:
                for item, count in Counter(supported_weights).items():
                    if count == 1:
                        single_weight = item
                    else:
                        mult_weight = item
                single_program_index = supported_weights.index(single_weight)
                balancing_weight = \
                    mult_weight - single_weight + initial_weights[supported_nodes[program][single_program_index]]
                # return early if balancing weight is found
                return None
            final_weights[program] = sum(supported_weights) + initial_weights[program]
            return final_weights[program]

    for program in supported_nodes:
        if program not in final_weights:
            get_program_final_weight(program)
    return balancing_weight


def run_test():
    inp_test = get_multi_line_input('input_test')
    assert bottom(inp_test) == 'tknk'
    supported_nodes, initial_weights = parse(inp_test)
    assert compute_total_weight(supported_nodes, initial_weights) == 60


def main():
    run_test()
    inp = get_multi_line_input('input')
    print bottom(inp)
    supported_nodes, initial_weights = parse(inp)
    print compute_total_weight(supported_nodes, initial_weights)


if __name__ == '__main__':
    main()
