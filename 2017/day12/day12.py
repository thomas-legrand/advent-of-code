from collections import defaultdict


def get_multi_line_input(f_name):
    f = open(f_name)
    return f.read().splitlines()


def run_test():
    test_inp = get_multi_line_input('test_input')
    g = create_graph(test_inp)
    assert len(perform_bfs(g, 0)) == 6


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


def perform_bfs(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


def find_groups(g):
    ng = set()
    for v in g:
        ng.add(frozenset(perform_bfs(g, v)))
    return len(ng)


def main():
    run_test()
    inp = get_multi_line_input('input')
    g = create_graph(inp)
    print len(perform_bfs(g, 0))
    print find_groups(g)


if __name__ == '__main__':
    main()
