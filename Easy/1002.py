class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        new_set = set(words[0])
        for i in range(1, len(words)):
            new_set = new_set & set(words[i])
            
        print(new_set)
        for i in new_set:
            countList = []
            for j in range(len(words)):
                countList.append(words[j].count(i))

            for j in range(min(countList)):
                ans.append(i)
            print(ans)
            
        return ans