class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0, 1, 1]
        for i in range(2, n):
            seq.append(seq[i-2]+seq[i-1]+seq[i])

        return seq[n]