# Solution with stack data structure
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

        return stack[-1]
