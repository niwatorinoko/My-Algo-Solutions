class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0]*num_people
        num = 0
        while candies > 0:
            for i in range(num_people):
                num += 1
                if candies < num:
                    ans[i] += candies
                    candies = 0
                else:
                    ans[i] += num
                    candies -= num
        return ans