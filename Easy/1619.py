class Solution:
    def trimMean(self, arr: List[int]) -> float:
        for i in range(int(len(arr)*0.05)):
            arr.remove(max(arr))
            arr.remove(min(arr))
        return sum(arr)/len(arr)