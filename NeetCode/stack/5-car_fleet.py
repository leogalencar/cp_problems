# Solution with O(n) time complexity and O(n) space complexity. We first create a list of tuples containing the position and speed of each car, and sort it in reverse order based on the position. We then iterate through the sorted list and calculate the time it takes for each car to reach the target. If the current car takes more time than the previous car, it forms a new fleet, and we update the previous time to the current time. Finally, we return the total number of fleets formed.
# Time complexity: O(n log n) due to sorting, where n is the number of cars.
# Space complexity: O(n) for the list of tuples storing the position and speed of each car.


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        fleets = 1
        prevTime = (target - cars[0][0]) / cars[0][1]
        for i in range(1, n):
            currTime = (target - cars[i][0]) / cars[i][1]
            if currTime > prevTime:
                prevTime = currTime
                fleets += 1

        return fleets
