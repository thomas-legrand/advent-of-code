import hashlib


def zeros_hash(key, num_zeros):
    c = 0
    while True:
        h = hashlib.md5(key + str(c)).hexdigest()
        if h[:num_zeros] == '0' * num_zeros:
            return c
        c += 1


def run_test():
    assert zeros_hash('abcdef', 5) == 609043
    assert zeros_hash('pqrstuv', 5) == 1048970


def main():
    run_test()
    secret_key = 'iwrupvqb'
    print zeros_hash(secret_key, 5)
    print zeros_hash(secret_key, 6)


if __name__ == '__main__':
    main()
