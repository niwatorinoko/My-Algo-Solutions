class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_x = m
        min_y = n
        for i in ops:
            if i[0] < min_x:
                min_x = i[0]
            if i[1] < min_y:
                min_y = i[1]
        return min_x*min_y

        #opsで当てはまる範囲を毎回狭めていくイメージ、、？