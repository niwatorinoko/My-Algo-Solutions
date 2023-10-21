class Solution:
    def reorderSpaces(self, text: str) -> str:
        if " " not in list(text):
            return text
        space = 0
        for i in list(text):
            if i == " ":
                space += 1
        split = text.split()
        if len(split) == 1:
            return split[0] + " "*space
        new_space = space//(len(text.split())-1)
        end = space%(len(split)-1)
        ans = split[0]
        for i in range(1, len(split)):
            ans += " "*new_space
            ans += split[i]
        return ans+" "*end