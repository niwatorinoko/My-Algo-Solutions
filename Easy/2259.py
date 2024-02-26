class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        numLi = []
        for i in range(len(number)):
            if number[i] == digit:
                numLi.append(int(number[:i]+number[i+1:]))
        return str(max(numLi))