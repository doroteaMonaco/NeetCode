from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next: # find the middle of the linked list
            slow = slow.next
            fast = fast.next.next

        second = slow.next # reverse the second half of the linked list
        slow.next = None # split the linked list into two halves

        rev = second
        prec = None
        while rev: # reverse the second half of the linked list
            next_node = rev.next
            rev.next = prec
            prec = rev
            rev = next_node

        first = head
        second = prec

        while second: # merge the two halves of the linked list alternately
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

        return None

# Time complexity: O(n)
# Space complexity: O(1)
              