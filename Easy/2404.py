class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = Counter(nums)
        count = 0
        ans = -1
        print(d)
        for key in sorted(d.keys()):
            if key%2 == 0:
                if d[key] > count:
                    ans = key
                    count = d[key]
        return ans