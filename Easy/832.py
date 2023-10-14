class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in image:
            temp = []
            for j in reversed(i):
                if j==0:
                    temp.append(1)
                else:
                    temp.append(0)
            ans.append(temp)
        return ans