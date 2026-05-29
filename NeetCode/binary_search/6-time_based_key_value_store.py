# Solution with binary search to find the value with the largest timestamp less than or equal to the given timestamp.
# Time complexity: O(log n) for get and O(1) for set.
# Space complexity: O(n * m) where n is the number of keys and m is the number of timestamps for each key.


class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        max_val, values = "", self.store.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            time, val = values[m]

            if time > timestamp:
                r = m - 1
            elif time < timestamp:
                l = m + 1
                max_val = val
            else:
                return val

        return max_val
