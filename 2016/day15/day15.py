import re
from typing import List


class Disk(object):
    def __init__(self, number, initial_position, total_positions):
        self.number = number
        self.initial_position = initial_position
        self.total_positions = total_positions

    def goes_through(self, drop_time: int) -> bool:
        return (self.initial_position + drop_time + self.number) % self.total_positions == 0


def get_disk_from_instructions(instructions: str) -> Disk:
    matches = re.findall("""\d+""", instructions)
    assert len(matches) == 4
    number = int(matches[0])
    total_positions = int(matches[1])
    initial_position = int(matches[3])
    return Disk(number, initial_position, total_positions)


def get_input(input_path):
    directions = open(input_path)
    rows = directions.readlines()
    return [r.strip("\n") for r in rows]


def get_first_possible_drop_time(input_disks: List[str]) -> int:
    disks = [get_disk_from_instructions(inst) for inst in input_disks]
    i = 0
    while any([not d.goes_through(i) for d in disks]):
        i += 1
    return i



def run_test():
    testDisk1 = get_disk_from_instructions("Disc #1 has 5 positions; at time=0, it is at position 4.")
    testDisk2 = get_disk_from_instructions("Disc #2 has 2 positions; at time=0, it is at position 1.")
    assert testDisk1.number == 1 and testDisk1.initial_position == 4 and testDisk1.total_positions == 5
    assert testDisk2.number == 2 and testDisk2.initial_position == 1 and testDisk2.total_positions == 2

    # If you press the button exactly at time=0, the capsule would start to fall;
    # it would reach the first disc at time=1. Since the first disc was at position 4 at time=0, by time=1
    # it has ticked one position forward. As a five-position disc, the next position is 0, and the capsule falls
    # through the slot.
    # Then, at time=2, the capsule reaches the second disc. The second disc has ticked forward two positions at
    # this point: it started at position 1, then continued to position 0, and finally ended up at position 1 again.
    # Because there's only a slot at position 0, the capsule bounces away.
    # If, however, you wait until time=5 to push the button, then when the capsule reaches each disc,
    # the first disc will have ticked forward 5+1 = 6 times (to position 0), and the second disc will have ticked
    # forward 5+2 = 7 times (also to position 0). In this case, the capsule would fall through the discs and come out
    # of the machine.

    assert testDisk1.goes_through(0)
    assert not testDisk2.goes_through(0)
    assert testDisk1.goes_through(5)
    assert testDisk2.goes_through(5)

    test_disks = get_input("test")
    assert get_first_possible_drop_time(test_disks) == 5


def main():
    run_test()
    input_disks = get_input("input")
    print(get_first_possible_drop_time(input_disks))
    input_disks.append("Disc #7 has 11 positions; at time=0, it is at position 0.")
    print(get_first_possible_drop_time(input_disks))


if __name__ == '__main__':
    main()