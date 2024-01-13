class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mon = {5:0,10:0}
        for bill in bills:
            if bill == 5:
                mon[5] += 1
            elif bill == 10:
                mon[10] += 1
                if mon[5] == 0:
                    print(bill)
                    return False
                else:
                    mon[5] -= 1
            elif bill == 20:
                if mon[5] >= 1 and mon[10] >= 1:
                    mon[5] -= 1
                    mon[10] -= 1
                elif mon[5] >= 3:
                    mon[5] -= 3
                else:
                    return False
        return True