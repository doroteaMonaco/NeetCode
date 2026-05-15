from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = ListNode()
        curr.next = head # create a dummy node to handle edge cases where the head needs to be removed

        slow = curr
        fast = curr

        for _ in range(n): # move the fast pointer n steps ahead
            fast = fast.next

        while fast.next: # move both pointers until the fast pointer reaches the end of the linked list
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next # remove the nth node from the end of the linked list
        return curr.next # return the head of the modified linked list, which is the next node of the dummy node

# Time complexity: O(n)
# Space complexity: O(1)
