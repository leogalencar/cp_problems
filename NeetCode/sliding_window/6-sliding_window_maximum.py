# Solution with two pointers and a deque to maintain the indices of the maximum elements in the current window. The right pointer (r) iterates through the list, while the left pointer (l) keeps track of the start of the current window. The deque is used to store indices of elements in decreasing order, ensuring that the maximum element is always at the front of the deque. When the right pointer moves, we remove indices from the back of the deque if they correspond to smaller elements than the current element. We also remove indices from the front of the deque if they are out of the current window. Finally, when we have a valid window (when r + 1 >= k), we append the maximum element (the front of the deque) to our result list.
# Time complexity: O(n) where n is the number of elements in the input list, since each element is processed at most twice (once when added to the deque and once when removed).
# Space complexity: O(n)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

        return res
