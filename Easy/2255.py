class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        """
        for i in words:
            for j in range(len(i)):
                if j >= len(s):
                    break
                if i[j] != s[j]:
                    break
            else:
                count += 1
        return count
        """
        for i in words:
            if s[0:len(i)] == i:
                count += 1
        return count