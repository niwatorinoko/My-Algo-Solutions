class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(int)
        ans = 0
        for a, b in dominoes:
            if a > b:
                pair = [a,b]
                counter[tuple(pair)] += 1
            else:
                pair = [b,a]
                counter[tuple(pair)] += 1
        print(counter)
        for i in counter.values():
            if i >= 2:
                ans += i*(i-1)//2
        return ans