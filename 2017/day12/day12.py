from collections import defaultdict
from common import bfs, input_utils as iu


def run_test():
    test_inp = iu.get_multi_line_input('test_input')
    g = create_graph(test_inp)
    assert len(bfs.perform_bfs(g, 0)) == 6


def create_graph(inp):
    graph = defaultdict(list)
    edges = [parse_edge(e) for e in inp]
    for e in edges:
        graph[e[0]] += e[1]
        for o in e[1]:
            graph[o].append(e[0])
    return graph


def parse_edge(edge):
    v0, v1 = edge.split(' <-> ')
    return int(v0), [int(v) for v in v1.split(',')]


def find_groups(g):
    ng = set()
    for v in g:
        ng.add(frozenset(bfs.perform_bfs(g, v)))
    return len(ng)


def main():
    run_test()
    inp = iu.get_multi_line_input('input')
    g = create_graph(inp)
    print len(bfs.perform_bfs(g, 0))
    print find_groups(g)


if __name__ == '__main__':
    main()
