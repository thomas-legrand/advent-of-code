NUM_ITERATIONS = 2017
STEPS = 355
STEPS_TEST = 3


def run_spinlock(steps):
    spinlock = [0]
    val = 1
    new = 0
    while val <= 2017:
        new = (steps + new) % len(spinlock) + 1
        spinlock = spinlock[:new] + [val] + spinlock[new:]
        val += 1
    return spinlock[new + 1]


def run_test():
    print run_spinlock(STEPS_TEST)


def main():
    run_test()
    print run_spinlock(STEPS)

if __name__ == '__main__':
    main()
