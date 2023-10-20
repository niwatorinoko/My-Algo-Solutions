class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        arr1Count = Counter(arr1)
        for i in arr2:
            ans += [i]*arr1Count[i]

        arr = []
        for i in arr1:
            if i not in ans:
                arr.append(i)

        ans = ans + sorted(arr)
        return ans