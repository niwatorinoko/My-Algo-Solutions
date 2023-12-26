class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ansDict = dict()
        for i,j in items1:
            ansDict[i] = j
        
        for i,j in items2:
            if i in ansDict.keys():
                ansDict[i] += j
            else:
                ansDict[i] = j
        ansList = []
        for i,j in ansDict.items():
            ansList.append([i,j])
        return sorted(ansList)