class Maze:
    def __init__(self, puzzle_input=1362):
        self.start_x = 1
        self.start_y = 1
        self.puzzle_input = puzzle_input

    def is_wall(self, t):
        x = t[0]
        y = t[1]
        s = x * x + 3 * x + 2 * x * y + y + y * y
        s += self.puzzle_input
        ones = bin(s).count("1")
        return ones % 2 != 0

    def next_valid_positions(self, t):
        x = t[0]
        y = t[1]
        possible = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        feasible = [(p[0], p[1], t[2] + 1) for p in possible if not self.is_wall(p) and p[0] >= 0 and p[1] >= 0]
        return feasible

    def run_bfs(self):
        boundary = [(1, 1, 0)]
        visited = {}
        while len(boundary) > 0:
            position = boundary.pop()
            visited[(position[0], position[1])] = position[2]
            boundary += [pos for pos in self.next_valid_positions(position) if not (pos[0], pos[1]) in visited
                         or visited[(pos[0], pos[1])] > pos[2]]
        return visited


def run_test():
    maze = Maze(puzzle_input=10)
    y = 0
    for x in range(10):
        t = (x, y)
        if x in [0, 2, 7]:
            assert not maze.is_wall(t)
        else:
            assert maze.is_wall(t)
    visited = maze.run_bfs()
    assert visited[(7, 4)] == 11


def main():
    run_test()
    maze = Maze()
    visited = maze.run_bfs()
    # part 1
    print(visited[(31, 39)])
    # part 2
    print(len([visited[x] for x in visited if visited[x] <= 50]))

if __name__ == '__main__':
    main()
