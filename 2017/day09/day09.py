def get_input():
    f = open('input')
    return f.readline()


PARENT_OPEN = '{'
PARENT_CLOSE = '}'
GARB_OPEN = '<'
GARB_CLOSE = '>'
IGNORE = '!'


def score_string(s):
    i = 0
    stack = []
    score = 0
    garbage = 0
    while i < len(s):
        if stack and stack[-1] == GARB_OPEN:
            if s[i] == IGNORE:
                i += 1
            elif s[i] == GARB_CLOSE:
                stack.pop()
            else:
                garbage += 1
        else:
            if s[i] == PARENT_OPEN:
                stack.append(PARENT_OPEN)
            elif s[i] == PARENT_CLOSE and stack[-1] == PARENT_OPEN:
                score += len(stack)
                stack.pop()
            elif s[i] == GARB_OPEN:
                stack.append(GARB_OPEN)
            elif s[i] == IGNORE:
                i += 1
        i += 1
    return score, garbage


def run_test():
    assert score_string('{{<a!>},{<a!>},{<a!>},{<ab>}}') == (3, 17)
    assert score_string('{{<!!>},{<!!>},{<!!>},{<!!>}}') == (9, 0)
    assert score_string('<{o"i!a,<{i<a>') == (0, 10)


def main():
    run_test()
    inp = get_input()
    print score_string(inp)

if __name__ == '__main__':
    main()
