class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        w = ""
        for i in words:
            w += i
        count = collections.Counter(w)

        for i in count.values():
            if i % len(words) != 0:
                return False
        return True