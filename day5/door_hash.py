import hashlib


PASSWORD_LENGTH = 8


def is_good_hash(s):
    return s.startswith("00000")


def get_hash(s):
    return hashlib.md5(s).hexdigest()


def compute_password(input_door_id):
    password = ""
    counter = 0
    while len(password) < 8:
        h = get_hash(input_door_id + str(counter))
        if is_good_hash(h):
            password += h[5]
            print password
        if counter % 100000 == 0:
            print counter
        if counter == 3231929:
            print input_door_id + str(counter)
            print h
            print is_good_hash(h)
        counter += 1

    return password


def compute_password2(input_door_id):
    password = [" "] * 8
    counter = 0
    # filled = 0
    while " " in password:
        h = get_hash(input_door_id + str(counter))
        if counter % 100000 == 0:
            print counter
        counter += 1
        # check if hash is good (i.e. starts with five 0s)
        if not is_good_hash(h):
            continue
        # check if the 6th character is a digit. if yes, it will be the position digit.
        if not h[5].isdigit():
            continue
        i = int(h[5])
        # check if our position digit is in the correct range
        if not i in range(8):
            continue
        # check if that position in the password has already been filled. If yes, ignore
        if password[i] != " ":
            continue
        # fill 7th character in the password at the 6th position, that was previously empty
        password[i] = h[6]
        print password
    return "".join(password)


def run_tests():
    assert get_hash("abc3231929")[5] == "1"
    assert get_hash("abc5017308")[:9] == "000008f82"
    # the following takes a little bit of time to run
    # assert compute_password("abc") == "18f47a30"
    assert compute_password2("abc") == "05ace8e3"


def main():
    run_tests()
    input_door_id = "ojvtpuvg"
    # print compute_password(input_door_id)
    print compute_password2(input_door_id)


if __name__ == '__main__':
    main()
