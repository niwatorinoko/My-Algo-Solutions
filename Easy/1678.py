class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        st = ""
        for i in command:
            if i == "G":
                ans += i
            elif i == ")":
                if st == "(":
                    ans += "o"
                    st = ""
                else:
                    ans += "al"
                    st = ""
            else:
                st += i
        return ans