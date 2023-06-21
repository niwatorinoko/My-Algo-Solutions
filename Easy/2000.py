class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        for i in range(len(word)):
            if word[i] == ch:
                reverse = ""
                for j in word[:i+1]:
                    reverse = j + reverse
                temp = word[i+1:]
                return reverse+temp