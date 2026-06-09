# Solution with time complexity O(n*k) and space complexity O(1).
# Time complexity: O(n*k) where n is the total number of nodes and k is the group size.
# Space complexity: O(1) for the linked list operations.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_list = []
        pointers = []
        dummy = ListNode()

        for l in lists:
            pointers.append(l)

        while len(pointers) > 0:
            minimum_idx = 0
            minimum_value = float("inf")
            if not pointers[minimum_idx]:
                pointers.pop(minimum_idx)
                continue
            for i, p in enumerate(pointers):
                if p and p.val < minimum_value:
                    minimum_idx, minimum_value = i, p.val
            res_list.append(minimum_value)
            pointers[minimum_idx] = pointers[minimum_idx].next

        cur = dummy
        i = 0
        for i in range(len(res_list)):
            cur.next = ListNode(res_list[i])
            cur = cur.next
        return dummy.next
