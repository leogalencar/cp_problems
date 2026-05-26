# Solution with two stacks: one for the actual stack and another for keeping track of the minimum values.
# Time complexity: O(1) for all operations (push, pop, top, getMin)
# Space complexity: O(n) in the worst case when all elements are the same and we need to store them in the minStack.


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
