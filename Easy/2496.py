class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        val_li = []
        for i in strs:
            if i.isdigit():
                val_li.append(int(i))
            else:
                val_li.append(len(i))
        return max(val_li)