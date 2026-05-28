# Solution with binary search to find the minimum eating speed K that allows Koko to eat all the bananas within H hours.
# Time complexity: O(N log M), where N is the number of piles and M is the maximum number of bananas in a pile.
# Space complexity: O(1)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            k = l + ((r - l) // 2)
            needed_hours = 0

            for p in piles:
                needed_hours += -(-p // k)

            if needed_hours > h:
                l = k + 1
            else:
                r = k - 1
                min_k = min(min_k, k)

        return min_k
