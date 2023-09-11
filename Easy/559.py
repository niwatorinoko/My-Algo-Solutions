class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        li = list(set(list1)&set(list2))
        m = list1.index(li[0]) + list2.index(li[0])
        ans = [li[0]]
        for i in range(1, len(li)):
            if list1.index(li[i]) + list2.index(li[i]) == m:
                ans.append(li[i])
            elif list1.index(li[i]) + list2.index(li[i]) < m:
                m = list1.index(li[i]) + list2.index(li[i])
                ans = [li[i]]
        return ans