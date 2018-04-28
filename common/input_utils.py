def get_input(f_name):
    f = open(f_name)
    return f.readline()


def get_multi_line_input(f_name):
    f = open(f_name)
    return f.read().splitlines()


def get_comma_separated_single_line_input(f_name):
    f = open(f_name)
    return f.readline().split(',')
