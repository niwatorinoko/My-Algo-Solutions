class Solution:
    def checkString(self, s: str) -> bool:
        flag = True
        for i in s:
            if i == "b":
                flag = False
            elif flag == False and i == "a":
                return False
        return True