from typing import List


class Tiles(object):
    def __init__(self, s: str, height: int):
        self.width = len(s)
        self.height = height
        self.tiles = [[True] * self.width] * self.height
        self.tiles[0] = [c == '^' for c in s]

    def __str__(self):
        x = [" ".join(map(lambda x: '^' if x else '.', row)) for row in self.tiles]
        return "\n".join(x)

    def is_trap(self, relevant: List[bool]) -> bool:
        return (relevant[0] and not relevant[2]) or (relevant[2] and not relevant[0])

    def compute_row(self, previous_row: List[bool]) -> List[bool]:
        fict_row = [False] + previous_row + [False]
        return [self.is_trap(fict_row[i:i + 3]) for i in range(len(previous_row))]

    def populate(self):
        for i in range(self.height - 1):
            self.tiles[i+1] = self.compute_row(self.tiles[i])


def run_test():
    t = Tiles("..^^.", 3)
    assert t.compute_row([False, False, True, True, False]) == [False, True, True, True, True]
    assert t.compute_row([False, True, True, True, True]) == [True, True, False, False, True]
    t.populate()
    assert t.tiles[2] == [True, True, False, False, True]
    t = Tiles(".^^.^.^^^^", 10)
    t.populate()
    assert t.tiles[9] == [True, True, False, True, True, True, False, False, True, True]
    print(sum([not x for sub in t.tiles for x in sub]))


def main():
    run_test()
    t = Tiles(".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^", 40)
    t.populate()
    print(sum([not x for sub in t.tiles for x in sub]))

    newt = Tiles(".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^", 400000)
    newt.populate()
    print(sum([not x for sub in newt.tiles for x in sub]))


if __name__ == '__main__':
    main()
