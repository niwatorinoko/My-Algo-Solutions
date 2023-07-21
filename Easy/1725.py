class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squaresLength = []
        for i in rectangles:
            if i[0] > i[1]:
                squaresLength.append(i[1])
            else:
                squaresLength.append(i[0])
        return squaresLength.count(max(squaresLength))
