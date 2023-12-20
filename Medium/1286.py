class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.li = [''.join(comb) for comb in itertools.combinations(characters, combinationLength)]
        self.combinationLength = combinationLength
        self.p = 0

    def next(self) -> str:
        temp = self.li[self.p]
        self.p += 1
        return temp

    def hasNext(self) -> bool:
        if self.p >= len(self.li):
            return False
        return True
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()