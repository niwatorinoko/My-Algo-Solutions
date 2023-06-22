class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in details:
            print(i[-4:-2])
            if int(i[-4:-2])>60:
                res+=1
        return res