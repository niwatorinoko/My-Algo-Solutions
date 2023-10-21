class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = dict()
        for i in range(lowLimit, highLimit+1):
            boxnum = 0
            for j in str(i):
                boxnum += int(j)
            if boxnum in box.keys():
                box[boxnum] += 1
            else:
                box[boxnum] = 1
    
        return max(box.values())
        