class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        words = []
        for i in s:
            if i != " ":
                word += i
            else:
                if len(word) > 0:
                    words = [word] + words
                    word = ""
        if len(word) > 0:
            words = [word] + words
        return " ".join(words)