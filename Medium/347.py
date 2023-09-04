class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)
        print(type(numsCounter))
        ans = []
        for i in range(k):
            ans.append(numsCounter[i][0])
        return ans