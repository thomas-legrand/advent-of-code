from string import ascii_uppercase


def get_multi_line_input():
    f = open('input')
    return f.read().splitlines()


def format_network(inp):
    max_i = max(map(len, inp))
    max_j = len(inp)
    network = [[0 for _ in range(max_i)] for _ in range(max_j)]
    for j in range(max_j):
        for i in range(max_i):
            if i < len(inp[j]):
                network[j][i] = inp[j][i]
            else:
                network[j][i] = " "
    return network


def find_origin(network):
    max_i = len(network[0])
    max_j = len(network)
    for i in [0, max_i - 1]:
        for j in range(max_j):
            if network[j][i] == "-":
                return [i, j]
    for j in [0, max_j - 1]:
        for i in range(max_i):
            if network[j][i] == "|":
                return [i, j]


def follow(network):
    steps = 0
    letters = ""
    max_i = len(network[0])
    max_j = len(network)
    position = find_origin(network)
    if position[0] == 0:
        dir = [1, 0]
    elif position[1] == 0:
        dir = [0, 1]
    elif position[0] == max_i:
        dir = [-1, 0]
    elif position[1] == max_j:
        dir = [0, -1]
    while True:
        if network[position[1]][position[0]] == "+":
            if dir[1] == 0:
                for j in [-1, 1]:
                    if 0 <= position[1] + j < max_j and network[position[1] + j][position[0]] == "|":
                        dir[1] = j
                        dir[0] = 0
            elif dir[0] == 0:
                for i in [-1, 1]:
                    if 0 <= position[0] + i < max_i and network[position[1]][position[0] + i] == "-":
                        dir[0] = i
                        dir[1] = 0
        elif network[position[1]][position[0]] in ascii_uppercase:
            letters += network[position[1]][position[0]]
        else:
            if not network[position[1]][position[0]] in ["-", "|"]:
                print "done in {} steps".format(steps)
                break
        position[0] += dir[0]
        position[1] += dir[1]
        steps += 1
    return letters


def main():
    inp = get_multi_line_input()
    network = format_network(inp)
    print follow(network)

if __name__ == '__main__':
    main()
