class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for i in range(len(nums)):
            if i%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        even = sorted(even)
        odd = sorted(odd) 
        odd.reverse() 

        ans = []
        for i in range(min(len(even),len(odd))):
            ans.append(even[i])
            ans.append(odd[i])
        if len(odd) > len(even):
            print("odd",odd[len(even)+1:])
            ans += odd[len(even):]
        elif len(odd) < len(even):
            print("even",even[len(odd)+1:])
            ans += even[len(odd):]

        return ans