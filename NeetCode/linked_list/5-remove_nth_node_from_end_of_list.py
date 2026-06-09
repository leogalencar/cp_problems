# Solution with two pointers, one pointer is n nodes ahead of the other pointer. When the first pointer reaches the end of the list, the second pointer will be at the node before the node to be removed. We can then skip the node to be removed by changing the next pointer of the second pointer.
# Time complexity: O(n)
# Space complexity: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
