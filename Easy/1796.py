class Solution:
    def secondHighest(self, s: str) -> int:
        numset = set()
        for i in s:
            if i.isdigit():
                numset.add(int(i))
        
        if len(numset) == 0:
            return -1

        numset.remove(max(numset))

        if len(numset) == 0:
            return -1

        return max(numset)