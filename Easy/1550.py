class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)-2):
            for j in arr[i:i+3]:
                if j%2 == 0:
                    break
            else:
                return True        
        return False