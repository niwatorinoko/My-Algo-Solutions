class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_array = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ans = 0
        count = 0
        for i,j in sorted_array:
            if count+i < truckSize:
                ans += (i*j)
                count += i
            else:
                ans += (truckSize-count)*j
                break
        return ans