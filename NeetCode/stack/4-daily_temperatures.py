# Solution with stack data structure
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # pair: [temp, index]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append((t, i))
        return res
