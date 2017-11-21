from collections import defaultdict


def get_multi_line_input():
    f = open('input')
    return f.read().splitlines()


def is_nice(s):
    three_vowels = len(filter(lambda x: x in 'aeiou', s)) > 2
    twice_in_a_row = False
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            twice_in_a_row = True
    no_bad_string = all([x not in s for x in ['ab', 'cd', 'pq', 'xy']])
    return three_vowels and twice_in_a_row and no_bad_string


def is_nice_2(s):
    twograms = defaultdict(list)
    for i in range(0, len(s) - 1):
        twograms[s[i:i+2]].append(i)
    cond1 = len(filter(lambda x: len(x) > 1 and max(x) - min(x) > 1, twograms.values())) > 0
    cond2 = False
    for i in range(0, len(s) - 2):
        if s[i] == s[i+2]:
            cond2 = True
    return cond1 and cond2


def run_test():
    assert is_nice('ugknbfddgicrmopn')
    assert is_nice('aaa')
    assert not is_nice('jchzalrnumimnmhp')
    assert not is_nice('haegwjzuvuyypxyu')
    assert not is_nice('dvszwmarrgswjxmb')
    assert is_nice_2('qjhvhtzxzqqjkmpb')
    assert is_nice_2('xxyxx')
    assert not is_nice_2('aaa')
    assert not is_nice_2('uurcxstgmygtbstg')
    assert not is_nice_2('ieodomkazucvgmuy')


def main():
    run_test()
    inp = get_multi_line_input()
    print sum(map(is_nice, inp))
    print sum(map(is_nice_2, inp))

if __name__ == '__main__':
    main()
