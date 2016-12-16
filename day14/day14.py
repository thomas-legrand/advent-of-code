import hashlib
import re
from collections import defaultdict


class OneTimePad:
    pattern3 = r"""(.)\1\1"""
    pattern5 = r"""(.)\1\1\1\1"""

    def __init__(self, salt):
        self.salt = salt
        self.triples_table = defaultdict(list)
        self.fiveofakind_table = defaultdict(list)
        self.keys = []

    def getmd5(self, i):
        s = self.salt + str(i)
        return hashlib.md5(s.encode('utf-8')).hexdigest()

    def get_triple_fives(self, i):
        h = self.getmd5(i)
        return re.findall(self.pattern3, h), re.findall(self.pattern5, h)

    def populate(self, limit):
        i = 0
        while i <= limit:
            triples, fives = self.get_triple_fives(i)
            if len(triples) > 0:
                print(i)
                self.triples_table[triples[0]].append(i)
            if len(fives) > 0:
                for five in fives:
                    self.fiveofakind_table[five].append(i)
            i += 1

    def find_keys(self):
        for triple in self.triples_table:
            if triple in self.fiveofakind_table:
                triple_indices = self.triples_table[triple]
                five_indices = self.fiveofakind_table[triple]
                for i in triple_indices:
                    if len([f for f in five_indices if i < f <= i + 1000]) > 0 and i not in self.keys:
                        self.keys.append(i)
        self.keys.sort()


class OneTimePadStretching(OneTimePad):
    def getmd5(self, i):
        s = self.salt + str(i)
        for j in range(2017):
            s = hashlib.md5(s.encode('utf-8')).hexdigest()
        return s



def run_test():
    pad = OneTimePad("abc")

    # The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5....
    # However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes
    # (index 19 through index 1018) contain 88888.
    #  The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key:
    # one of the next thousand hashes (the one at index 816) contains eeeee.
    # None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200
    # contains 99999.
    # Eventually, index 22728 meets all of the criteria to generate the 64th key.

    triple, _ = pad.get_triple_fives(18)
    assert triple == ["8"]
    pad.populate(100000)
    assert 18 in pad.triples_table["8"]
    print(pad.fiveofakind_table["e"])
    assert 816 in pad.fiveofakind_table["e"]
    assert 39 in pad.triples_table["e"]
    pad.find_keys()
    assert len(pad.keys) > 64
    assert pad.keys[63] == 22728


def run_test2():
    pad = OneTimePadStretching("abc")
    assert pad.getmd5(0) == "a107ff634856bb300138cac6568c0f24"
    triple, _ = pad.get_triple_fives(5)
    assert "2" in triple
    triple, _ = pad.get_triple_fives(10)
    assert "e" in triple
    _, fives = pad.get_triple_fives(89)
    assert "e" in fives
    pad.populate(30000)
    pad.find_keys()
    assert len(pad.keys) > 64
    assert pad.keys[63] == 22551


def main():
    run_test()
    pad = OneTimePad("cuanljph")
    pad.populate(100000)
    pad.find_keys()
    assert len(pad.keys) > 64
    print(pad.keys[63])

    # run_test2()
    pad = OneTimePadStretching("cuanljph")
    pad.populate(30000)
    pad.find_keys()
    assert len(pad.keys) > 64
    print(pad.keys[63])

if __name__ == '__main__':
    main()
