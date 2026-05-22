# Solution with hash map and inverse hash map.
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        inv_hmap = {}

        for i in range(len(nums)):
            n = nums[i]

            if hmap.get(n, 0) != 0:
                inv_hmap[hmap[n]].remove(n)
            hmap[n] = hmap.get(n, 0) + 1
            inv_hmap.setdefault(hmap[n], []).append(n)

        count = 0
        tmp = []
        for v in reversed(inv_hmap.values()):
            if count == k:
                break
            tmp.append(v)
            count += len(v)

        res = [item for sublist in tmp for item in sublist]
        print(hmap)
        print(inv_hmap)
        return res
