
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev # find the kth node from the current groupPrev
            for _ in range(k): # move the kth pointer k steps ahead
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next # store the next node after the kth node

            prev = groupNext # reverse the nodes in the current group
            curr = groupPrev.next # start from the first node of the current group

            while curr != groupNext: # reverse the nodes until we reach the groupNext node
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next # store the first node of the current group, which will become the last node after reversal    
            groupPrev.next = kth # connect the previous part of the linked list to the new head of the reversed group
            groupPrev = tmp # move the groupPrev pointer to the last node of the reversed group, which is the new groupPrev for the next iteration
        
        return dummy.next
    
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(1) since we are reversing the linked list in place
        

