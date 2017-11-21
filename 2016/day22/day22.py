from collections import namedtuple


NodeUsage = namedtuple('NodeUsage', ['name', 'used', 'avail'])


def get_input(input_path):
    directions = open(input_path)
    rows = directions.readlines()
    nodes = [r.strip("\n").split() for r in rows[2:]]
    return {node[0]: NodeUsage(name=node[0], used=int(node[2][:-1]), avail=int(node[3][:-1])) for node in nodes}


def get_viable_pairs(nodes):
    return [(node1.name, node2.name) for node1 in nodes for node2 in nodes if node1.name != node2.name and 0 < node1.used < node2.avail]

def run_tests():
    pass


def main():
    run_tests()
    nodes = get_input("input")
    nodes_values = nodes.values()
    print(len(get_viable_pairs(nodes_values)))


if __name__ == '__main__':
    main()