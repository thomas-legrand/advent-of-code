import os


def get_input_rows(input_path):
    directions = open(input_path)
    instructions_string = directions.readlines()
    return [[int(i) for i in instruction.rstrip("\n").split()] for instruction in instructions_string]


def get_input_by_columns(input_path):
    triangles = get_input_rows(input_path)
    triangles_by_columns = [triangle[i] for i in xrange(3) for triangle in triangles]
    return [triangles_by_columns[x:x+3] for x in xrange(0, len(triangles_by_columns), 3)]


def is_triangle(candidate_triangle):
    assert len(candidate_triangle) == 3
    candidate_triangle.sort()
    return sum(candidate_triangle[:2]) > candidate_triangle[2]


def main():
    input_path = os.path.join('input', 'triangles')
    candidates_triangles = get_input_rows(input_path)
    real_triangles = [candidate for candidate in candidates_triangles if is_triangle(candidate)]
    print len(real_triangles)
    print real_triangles[:10]
    print len(candidates_triangles)
    print candidates_triangles[:10]

    candidates_triangles_by_columns = get_input_by_columns(input_path)
    real_triangles_by_columns = [candidate for candidate in candidates_triangles_by_columns if is_triangle(candidate)]
    print candidates_triangles_by_columns[:10]
    print len(real_triangles_by_columns)


if __name__ == '__main__':
    main()
