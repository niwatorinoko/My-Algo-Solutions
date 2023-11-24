class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time = [keysPressed[0], releaseTimes[0]]
        for i in range(1,len(releaseTimes)):
            if releaseTimes[i]-releaseTimes[i-1] > time[1]:
                time = [keysPressed[i], releaseTimes[i]-releaseTimes[i-1]]
            elif releaseTimes[i]-releaseTimes[i-1] == time[1]:
                if keysPressed[i] > time[0]:
                    time = [keysPressed[i], releaseTimes[i]-releaseTimes[i-1]]
        return time[0]