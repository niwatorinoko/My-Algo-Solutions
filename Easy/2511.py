class Solution:
    def captureForts(self, forts: List[int]) -> int:
        if 1 not in forts:
            return 0
        
        def isTrue(temp):
            if temp[0] == 1 and temp[-1] == -1:
                for i in range(1, len(temp)-1):
                    if temp[i] != 0:
                        return False
                else:
                    return True
            elif temp[0] == -1 and temp[-1] == 1:
                for i in range(1, len(temp)-1):
                    if temp[i] != 0:
                        return False
                else:
                    return True
            else:
                return False
        for i in range(len(forts)-1,0,-1):
            for j in range(len(forts)-i):
                temp = forts[j:j+i+1]
                if isTrue(temp):
                    return len(temp)-2
        return 0