import sys
sys.path.append("../..")
from common import input_utils as iu
from collections import defaultdict


def parse_graph(inp):
    g = defaultdict(dict)
    for i in range(len(inp)):
        conn1, conn2 = [int(v) for v in inp[i].split('/')]
        g[conn1][conn2] = i
        g[conn2][conn1] = i
    return g


def get_strongest(graph, node, visited):
    # should we take into account duplicate connectors?
    if node not in graph:
        return 0
    strongest = 0
    candidates = [n for n in graph[node] if graph[node][n] not in visited]
    for n in candidates:
        visited_copy = set(visited)
        visited_copy.add(graph[node][n])
        value = n + node + get_strongest(graph, n, visited_copy)
        if value > strongest:
            strongest = value
    return strongest


def run_test():
    inp = iu.get_multi_line_input('input_test')
    # print parse_graph(inp)
    assert get_strongest(parse_graph(inp), 0, set()) == 31


def main():
    run_test()
    inp = iu.get_multi_line_input('input')
    print get_strongest(parse_graph(inp), 0, set())

if __name__ == '__main__':
    main()
