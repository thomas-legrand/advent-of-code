import sys
sys.path.append("../..")
from common import input_utils

INITIAL_IMAGE = ['.#.', '..#', '###']


def divide(image):
    assert len(image) % 2 == 0 or len(image) % 3 == 0
    s = 2 if len(image) % 2 == 0 else 3
    rowsets = [image[i:i+s] for i in range(0, len(image), s)]
    new_img = []
    for rowset in rowsets:
        square = [row[i:i + s] for row in rowset for i in range(0, len(row), s)]
        new_img.append([square[i::len(image)/s] for i in range(len(image)/s)])
    return new_img


def rotate(img):
    return [''.join(i) for i in flip(zip(*img), rows=False)]


def flip(img, rows=True):
    if rows:
        return img[::-1]
    else:
        return map(lambda c: c[::-1], img)


def get_transforms(input_img):
    img = list(input_img)
    transforms = []
    for i in range(4):
        transforms.append(tuple(img))
        transforms.append(tuple(flip(img)))
        transforms.append(tuple(flip(img, rows=False)))
        img = rotate(img)
    return set(transforms)


def parse_rules(inp):
    parsed = [[j.split('/') for j in i.split(' => ')] for i in inp]
    return {t: p[1] for p in parsed for t in get_transforms(p[0])}


def enhance(img_structure, rules):
    return [[rules[tuple(i)] for i in img_list] for img_list in img_structure]


def consolidate(img_struct):
    return [''.join(z) for e in map(lambda x: zip(*x), img_struct) for z in e]


def count(img):
    return len(filter(lambda c: c == '#', ''.join(img)))


def run(inp, iterations=2):
    rules = parse_rules(inp)
    img = list(INITIAL_IMAGE)
    for i in range(iterations):
        img = divide(img)
        # print 'image after division: ' + str(img)
        img = enhance(img, rules)
        # print 'image after enhancement: ' + str(img)
        img = consolidate(img)
        # print 'image after consolidation: ' + str(img)
    return count(img)


def run_test():
    test_image = ['..##', '.#.#', '.###', '####']
    assert count(test_image) == 11
    assert divide(test_image) == [[['..', '.#'], ['##', '.#']], [['.#', '##'], ['##', '##']]]
    small_img = ['..', '.#']
    assert flip(small_img) == ['.#', '..']
    assert flip(small_img, rows=False) == ['..', '#.']
    assert rotate(small_img) == ['..', '#.']
    assert rotate(rotate(small_img)) == ['#.', '..']
    inp = input_utils.get_multi_line_input('test_input')
    # some checks
    # print enhance(divide(INITIAL_IMAGE), parse_rules(inp))
    # print consolidate([[['##.', '#..', '...'], ['##.', '#..', '...']], [['##.', '#..', '...'], ['##.', '#..', '...']]])
    assert run(inp) == 12


def main():
    run_test()
    inp = input_utils.get_multi_line_input('input')
    print run(inp, 5)
    print run(inp, 18)


if __name__ == '__main__':
    main()
