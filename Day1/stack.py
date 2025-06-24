class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
        else:
            self.stack.append(val)

    def pop(self) -> None:
            if not self.stack: return
            self.stack.pop()
       

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minval=float('inf')
        for num in self.stack:
            if num <minval:
                minval=num
        return minval
        #pretty simple just implementing a stack