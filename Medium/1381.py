class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.length = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.length:
            self.stack.append(x)
            

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack.pop(-1)
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack),k)):
            self.stack[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)