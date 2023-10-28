class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                print(words[i][::-1],words[j])
                if words[i][::-1] == words[j]:
                    count += 1
        return count