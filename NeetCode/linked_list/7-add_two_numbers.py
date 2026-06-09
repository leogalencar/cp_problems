# Solution with dummy node and carry variable to handle the addition of two numbers represented as linked lists.
# Time complexity: O(max(m, n)) where m and n are the lengths of the two linked lists.
# Space complexity: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            res = v1 + v2 + carry

            digit = res % 10
            carry = res // 10

            cur.next = ListNode(digit)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
