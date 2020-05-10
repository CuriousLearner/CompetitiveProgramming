# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        # Keep track of min val to get access in O(1) time.
        self.min_vals = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_vals or x <= self.min_vals[-1]:
            self.min_vals.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min_vals[-1]:
            self.min_vals.pop()
        return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
