# class MinStack:
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            if self.minstack[-1] >= val:
                self.minstack.append(val)
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.stack.pop()
            self.minstack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        # print(self.stack[-1])
        return(self.stack[-1])

    def getMin(self) -> int:
        # print(self.minstack[-1])
        return (self.minstack[-1])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
