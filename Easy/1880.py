class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        f = ""
        for i in firstWord:
            f += str(ord(i)-97)

        s = ""
        for i in secondWord:
            s += str(ord(i)-97)

        t = ""
        for i in targetWord:
            t += str(ord(i)-97)

        if int(t) != int(f) + int(s):
            return False
        return True