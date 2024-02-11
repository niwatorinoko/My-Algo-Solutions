class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_li = s.split()
        num = 0
        for word in s_li:
            if word.isdigit():
                if int(word) > num:
                    num = int(word)
                else:
                    return False
        return True