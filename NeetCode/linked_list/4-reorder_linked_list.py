# Solution with reversing the second half of the list and then merging the two halves together.
# Time complexity: O(n)
# Space complexity: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle point with slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next  # start of second half
        prev = slow.next = None  # disconnect the halves to avoid cycles and bugs

        # reverse the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
