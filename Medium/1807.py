class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_dict = {key: value for key, value in knowledge}
        ans, st, flag = "", "", False
        for i in s:
            if i == "(":
                flag = True
            elif i == ")":
                flag = False
                ans += knowledge_dict.get(st, "?")
                st = ""
            elif flag:
                st += i
            else:
                ans += i
        return ans