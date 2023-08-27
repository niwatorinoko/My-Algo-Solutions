class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False

        p = 0
        for i in range(1,len(arr)):
            if arr[i-1] == arr[i]:
                return False
            elif arr[i-1] > arr[i]:
                p = i
                break
        
        if p == 1:
            return False

        for j in range(p, len(arr)):
            if arr[j-1] == arr[j]:
                return False
            elif arr[j-1] < arr[j]:
                return False
        else:
            return True