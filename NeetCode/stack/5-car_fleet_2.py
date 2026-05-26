# Solution with stack to count the number of car fleets that will arrive at the target.
# Time complexity: O(n log n) due to sorting the cars based on their position. The rest of the operations are O(n).
# Space complexity: O(n) for the stack.


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        stack = []
        for p, s in cars:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
