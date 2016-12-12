from collections import defaultdict
import re


def get_input(input_path):
    directions = open(input_path)
    rows = directions.readlines()
    return [r.strip("\n") for r in rows]


def parse_input(instrutions):
    goes = defaultdict(list)
    gives = {}
    for inst in instrutions:
        if 'goes' in inst:
            matches = re.findall('(?:value|bot|output)\s\d+', inst)
            goes[matches[1]].append(matches[0])
        if 'gives' in inst:
            matches = re.findall('(?:value|bot|output)\s\d+', inst)
            gives[matches[0]] = [matches[1], matches[2]]
    return goes, gives


def assign_values(goes, gives):  # find length of complete lists, and full length.
    # get the set of 'bots', from gives keys and values.
    to_assign = set(gives.keys()).union({item for items in gives.values() for item in items if 'bot' in item})
    while len(to_assign) > 0:
        # unassigned output contains bots and output bin
        unassigned_output = [o for o in to_assign if len(goes[o]) == 2]
        for output in unassigned_output:
            destinations = gives[output]
            values = sorted(goes[output], key=lambda x: int(x.split(" ")[1]))
            goes[destinations[0]].append(values[0])
            goes[destinations[1]].append(values[1])
            to_assign.remove(output)
    return goes


def main():
    instrutions = get_input("input")
    goes, gives = parse_input(instrutions)
    final_goes = assign_values(goes, gives)
    print(final_goes)
    for f in final_goes:
        if 'value 61' in final_goes[f] and 'value 17' in final_goes[f]:
            print(f)
    print(final_goes['output 0'])
    print(final_goes['output 1'])
    print(final_goes['output 2'])


if __name__ == '__main__':
    main()
