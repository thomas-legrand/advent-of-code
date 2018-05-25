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


def parse_graph2(inp):
    g = defaultdict(dict)
    s = {}
    for i in range(len(inp)):
        conn1, conn2 = [int(v) for v in inp[i].split('/')]
        g[conn1][i] = conn2
        g[conn2][i] = conn1
        s[i] = [conn1, conn2]
    return g, s


def get_strongest(graph, node, visited):
    # should we take into account duplicate connectors?
    if node not in graph:
        return 0, [0]
    strongest = 0
    candidates = [n for n in graph[node] if graph[node][n] not in visited]
    for n in candidates:
        visited_copy = set(visited)
        visited_copy.add(graph[node][n])
        value = n + node + get_strongest(graph, n, visited_copy)
        if value > strongest:
            strongest = value
    return strongest


def get_longest(graph, start_node, conn):
    connectors_to_explore = [(c, [c], graph[start_node][c]) for c in graph[start_node].keys()]
    best_length = 0
    best_paths = []
    while connectors_to_explore:
        connector, connector_path, current_node = connectors_to_explore.pop()
        if len(connector_path) > best_length:
            best_paths = [connector_path]
            best_length = len(connector_path)
        elif len(connector_path) == best_length:
            best_paths.append(connector_path)
        candidate_connectors = [c for c in graph[current_node].keys() if c not in connector_path]
        for c in candidate_connectors:
            connectors_to_explore.append((c, connector_path + [c], graph[current_node][c]))
    return max(map(lambda c: get_strength_connector_path(c, conn), best_paths))


def get_strength_connector_path(connector_path, s):
    ss = 0
    for c in connector_path:
        ss += sum(s[c])
    return ss


def run_test():
    inp = iu.get_multi_line_input('input_test')
    # print parse_graph(inp)
    assert get_strongest(parse_graph(inp), 0, set()) == 31
    print parse_graph2(inp)
    graph, conn = parse_graph2(inp)
    assert get_longest(graph, 0, conn) == 19


def main():
    run_test()
    inp = iu.get_multi_line_input('input')
    print get_strongest(parse_graph(inp), 0, set())
    graph, conn = parse_graph2(inp)
    print get_longest(graph, 0, conn)

if __name__ == '__main__':
    main()
