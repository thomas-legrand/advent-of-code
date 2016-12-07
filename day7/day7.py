import os
import re


def get_input(input_path):
    directions = open(input_path)
    rows = directions.readlines()
    return rows


def is_abba(s):
    if len(s) < 4 or len(s) > 4:
        return False
    if s[0] == s[3] and s[1] == s[2] and s[0] != s[1]:
        return True
    return False


def contains_abba(s):
    for i in range(len(s) - 3):
        if is_abba(s[i:i + 4]):
            return True
    return False


def get_list(s):
    return re.findall(r"[\w]+", s)


def supports_tls(s):
    for l in get_list(s)[1::2]:
        if contains_abba(l):
            return False
    for l in get_list(s)[0::2]:
        if contains_abba(l):
            return True
    return False


def run_test():
    # abba[mnop]qrst supports TLS (abba outside square brackets).
    # abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    # aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    # ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
    assert is_abba('abba')
    assert not is_abba('aaaa')
    assert contains_abba('abba')
    assert not contains_abba('aaaa')
    assert contains_abba('ioxxoj')
    assert not contains_abba('ioxxxj')
    assert not contains_abba('ixxxxj')
    assert get_list('abba[mnop]qrst') == ['abba', 'mnop', 'qrst']
    assert supports_tls('abba[mnop]qrst')
    assert not supports_tls('bcd[bddb]xyyx')
    assert not supports_tls('aaaa[qwer]tyui')
    assert supports_tls('ioxxoj[asdfgh]zxcvbn')


def is_aba(s):
    if len(s) > 3 or len(s) < 3:
        return False
    if s[0] == s[2] and s[1] != s[0]:
        return True
    return False


def get_abas(s):
    res = set()
    for i in range(len(s) - 2):
        if is_aba(s[i:i + 3]):
            res.add(s[i:i + 3])
    return res


def supports_ssl(s):
    outside = get_list(s)[0::2]
    inside = get_list(s)[1::2]
    outside_aba = set()
    inside_aba = set()
    for s in outside:
        outside_aba = outside_aba.union(get_abas(s))
    for s in inside:
        inside_aba = inside_aba.union(get_abas(s))
    for o in outside_aba:
        for i in inside_aba:
            if o[0] == i[1] and o[1] == i[0]:
                return True
    return False


def run_test2():
    # aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    # xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    # aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    # zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
    assert supports_ssl('aba[bab]xyz')
    assert not supports_ssl('xyx[xyx]xyx')
    assert supports_ssl('aaa[kek]eke')
    assert supports_ssl('zazbz[bzb]cdb')


def main():
    run_test()
    input_path = os.path.join('input', 'data')
    print len([inp for inp in get_input(input_path) if supports_tls(inp)])
    run_test2()
    print len([inp for inp in get_input(input_path) if supports_ssl(inp)])


if __name__ == '__main__':
    main()
