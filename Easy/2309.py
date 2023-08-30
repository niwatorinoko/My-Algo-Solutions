class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ""
        for i in s:
            if i.islower():
                if i.upper() in s and ascii(i.upper()) > ascii(ans):
                    ans = i.upper()
            elif i.isupper() and ascii(i) > ascii(ans):
                if i.lower() in s:
                    ans = i
        return ans