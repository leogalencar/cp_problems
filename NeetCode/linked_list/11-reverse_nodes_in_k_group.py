# Solution with O(n) time complexity and O(1) space complexity. We reverse the linked list in k groups and connect the reversed segments together. We keep track of the first head of the linked list and the last node of the previous segment to connect it with the new head of the current segment. We also count the number of nodes in each segment to ensure we only reverse when there are at least k nodes remaining.
# Time complexity: O(n)
# Space complexity: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # while len(remaining_nodes) - k >= k:
        # for i in range(k):
        # reverse until k
        # go to head->next
        # return head

        first_head = head
        connect_node = None
        j = 0

        while True:
            cnt = 0

            # count nodes
            cur = head
            for i in range(k):
                if not cur:
                    print("not cur")
                    break
                cnt += 1
                cur = cur.next

            if not head:
                break

            if cnt < k:
                cur = first_head
                while cur.next:
                    cur = cur.next
                cur.next = head
                break

            # reverse nodes in k range
            cur = head
            prev = None
            for i in range(k):
                print(j, cur.val)
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            # prev is the new head of the linked list
            # cur is the head of the new segment [cur, ...]
            # head is the last value of prev k segment [prev, ..., head]
            if connect_node:
                connect_node.next = prev
            connect_node = head
            head = cur

            if j == 0:
                first_head = prev
            j += 1

        return first_head
