
class WhiteElephant(object):
    def __init__(self, number):
        self.number = number
        self.elves = list(range(number))

    def steal(self):
        while len(self.elves) > 1:
            if len(self.elves) % 2 == 0:
                self.elves = self.elves[::2]
            else:
                self.elves = self.elves[::2][1:]

    def steal_across(self):
        i = 0
        while len(self.elves) > 1:
            stolen = (i + len(self.elves) // 2) % len(self.elves)
            # print("current index %d and length %d" % (i, len(self.elves)))
            # print("will steal object %d at index %d" % (self.elves[stolen], stolen))
            del self.elves[stolen]
            if stolen < i:
                i -= 1
            if len(self.elves) - 1 <= i:
                i = 0
            else:
                i += 1


def run_tests():
    we = WhiteElephant(5)
    we.steal()
    assert we.elves == [2]

    we = WhiteElephant(5)
    we.steal_across()
    assert we.elves == [1]

    we = WhiteElephant(6)
    we.steal_across()
    assert we.elves == [2]

    we = WhiteElephant(7)
    we.steal_across()
    assert we.elves == [4]

    we = WhiteElephant(8)
    we.steal_across()
    assert we.elves == [6]


def main():
    run_tests()

    we = WhiteElephant(3012210)
    we.steal()
    print(we.elves[0] + 1)

    # this takes a good while
    we2 = WhiteElephant(3012210)
    we2.steal_across()
    print(we2.elves[0] + 1)


if __name__ == '__main__':
    main()
