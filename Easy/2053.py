class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l = 1
        for i in arr:
            if arr.count(i) == 1:
                if k == l:
                    return i
                else:
                    l += 1
        return ""