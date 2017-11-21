def parenthesis(seq_string, part):
    c = 0
    for i in range(len(seq_string)):
        if seq_string[i] == '(':
            c += 1
        else:
            c -= 1
        if part == 2 and c == -1:
            return i + 1

    if part == 1:
        return c


def run_test():
    assert parenthesis('(((())', 1) == 2
    assert parenthesis('))())()(((', 1) == 0
    assert parenthesis('(()', 1) == 1

    assert parenthesis('))())()(((', 2) == 1
    assert parenthesis('(()))', 2) == 5


def main():
    run_test()
    with open('input') as f:
        inp = f.readline()
        print parenthesis(inp, 1)
        print parenthesis(inp, 2)


if __name__ == '__main__':
    main()
