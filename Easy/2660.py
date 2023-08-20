class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        p1 = 0
        p1set = set()
        for i in range(n):
            if player1[i] == 10:
                p1set.add(i+1)        
                p1set.add(i+2)
        for i in range(n):
            if i in p1set:
                p1 += 2*player1[i]
            else:
                p1 += player1[i]

        p2 = 0
        p2set = set()
        for i in range(n):
            if player2[i] == 10:
                p2set.add(i+1)        
                p2set.add(i+2)
        for i in range(n):
            if i in p2set:
                p2 += 2*player2[i]
            else:
                p2 += player2[i]

        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0