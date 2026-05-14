from git import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False
            
        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
    
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(1)

# Others' solution: using a set to store visited nodes

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False
    
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(n) due to the set storing visited nodes