class MinStack:

    def __init__(self):
        self.minst = []

    def push(self, val: int) -> None:
        self.minst.append(val)

    def pop(self) -> None:
        self.minst.pop()

    def top(self) -> int:
        return self.minst[-1]

    def getMin(self) -> int:
        return min(self.minst)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()