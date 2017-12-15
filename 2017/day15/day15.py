GEN_A_FACTOR = 16807
GEN_B_FACTOR = 48271
MODULO = 2147483647

GEN_A_START_EX = 65
GEN_B_START_EX = 8921

GEN_A_START = 722
GEN_B_START = 354

MAX_PAIRS = 40000000
MAX_PAIRS_2 = 5000000


def to_bin(n):
    return str(bin(n))[-16:]


def match(n1, n2):
    return to_bin(n1) == to_bin(n2)


def gen_a(n):
    return (n * GEN_A_FACTOR) % MODULO


def gen_b(n):
    return (n * GEN_B_FACTOR) % MODULO


def process(max_n, a_start, b_start):
    c = 0
    a = a_start
    b = b_start
    for i in range(max_n):
        a = gen_a(a)
        b = gen_b(b)
        if match(a, b):
            c += 1
    return c


def process2(max_n, a_start, b_start):
    c = 0
    a = a_start
    b = b_start
    for i in range(max_n):
        a = gen_a(a)
        b = gen_b(b)
        while a % 4 != 0:
            a = gen_a(a)
        while b % 8 != 0:
            b = gen_b(b)
        if match(a, b):
            c += 1
    return c


def run_test():
    print to_bin(1092455)
    assert to_bin(1092455) == '1010101101100111'
    assert to_bin(430625591) == '1101001100110111'
    assert process2(MAX_PAIRS_2, GEN_A_START_EX, GEN_B_START_EX) == 309


def main():
    run_test()
    print process(MAX_PAIRS, GEN_A_START, GEN_B_START)
    print process2(MAX_PAIRS_2, GEN_A_START, GEN_B_START)


if __name__ == '__main__':
    main()
