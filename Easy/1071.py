import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        #import mathでgcd()で中に数字を入れると、最大公約数を返す
        return str1[:gcd(len(str1), len(str2))]