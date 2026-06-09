# Solution with a hash map to store the mapping from original nodes to their copies.
# Time complexity: O(n)
# Space complexity: O(n)


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        oldToCopy = defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.val = cur.val
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]
