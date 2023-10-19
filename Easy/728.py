class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            for j in str(i):
                if j == "0":
                    break
                if i%int(j) != 0:
                    break
            else:
                ans.append(i)
        return ans