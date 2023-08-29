class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        atitudes = [0,gain[0]]

        for i in range(1, len(gain)):
            atitudes.append(atitudes[i]+gain[i])


        return max(atitudes)