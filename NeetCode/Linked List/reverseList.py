# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next_node = curr.next # store the next node
            curr.next = prev # reverse the current node's pointer
            prev = curr # move the prev pointer one step forward
            curr = next_node # move the curr pointer one step forward

        return prev           
    

# Time complexity: O(n)
# Space complexity: O(1)

#Others' solution: recursive approach

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
    
# Time complexity: O(n)
# Space complexity: O(n) due to the recursive call stack