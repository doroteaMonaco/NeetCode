from git import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_new = ListNode()
        curr = head_new
        
        while list1 and list2:
            if list1.val >= list2.val:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
        while list1:
            curr.next = list1
            curr = curr.next
            list1 = list1.next
        while list2:
            curr.next = list2
            curr = curr.next
            list2 = list2.next
        return head_new.next
            
# Time complexity: O(n + m) where n and m are the lengths of the two lists
# Space complexity: O(1)