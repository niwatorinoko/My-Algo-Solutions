class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eat = len(candyType)//2
        types = len(set(candyType))
        if eat <= types:
            return eat
        return types