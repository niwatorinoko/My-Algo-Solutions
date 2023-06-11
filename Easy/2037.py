class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        res = 0
        #positionの大きい生徒から移動していく
        #moving from the student with largest positon
        for i in range(len(students)):
            studentIndex = students.index(max(students))
            position = max(seats)
            res += abs(position-students[studentIndex])
        #使用した値を消しておく。
        #Erase the value used 
            students[studentIndex] = 0
            seats.remove(position)
        return res