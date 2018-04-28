NUM_ITERATIONS = 2017
STEPS = 355
STEPS_TEST = 3
NUM_ITERATIONS_2 = 50000000


def run_spinlock(steps):
    spinlock = [0]
    val = 1
    new = 0
    while val <= NUM_ITERATIONS:
        new = (steps + new) % len(spinlock) + 1
        spinlock = spinlock[:new] + [val] + spinlock[new:]
        val += 1
    return spinlock[new + 1]


def run_spinlock2(steps):
    len_spinlock = 1
    val = 1
    new = 0
    pos_zero = 0
    last = 0
    while val <= NUM_ITERATIONS_2:
        new = (steps + new) % len_spinlock + 1
        len_spinlock += 1
        if new <= pos_zero:
            pos_zero += 1
        if new == pos_zero + 1:
            last = val
        val += 1
    return last


def run_test():
    assert run_spinlock(STEPS_TEST) == 638


def main():
    run_test()
    print run_spinlock(STEPS)
    print run_spinlock2(STEPS)

if __name__ == '__main__':
    main()
