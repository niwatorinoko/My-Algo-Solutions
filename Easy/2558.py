import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            chosen = max(gifts)
            sqrt = int(math.sqrt(chosen))
            gifts[gifts.index(chosen)] = sqrt
        return sum(gifts)