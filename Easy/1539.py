class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        p = 0
        num = 1

        while True:
            if arr[p] == num:
                p += 1
                num += 1
            else:
                count += 1
                num += 1
                print(num-1, count)

            if count == k:
                return num-1

            if len(arr)-1 < p:
                return k-count + num-1