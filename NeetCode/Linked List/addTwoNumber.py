from git import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2

        sumHead = ListNode(0)
        curr = sumHead
        carry = 0 

        while h1 or h2 or carry:
            x = h1.val if h1 else 0
            y = h2.val if h2 else 0
            total = x + y + carry 
            store = total % 10
            carry = total // 10
            new = ListNode(store)
            curr.next = new
            curr = curr.next
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None

        return sumHead.next

# Time complexity: O(max(n, m)) where n and m are the lengths of the two lists
# Space complexity: O(max(n, m)) due to the new list created to store the sum of the two numbers

#Other solution: using recursion
class Solution:
    def add(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        carry, val = divmod(v1 + v2 + carry, 10)

        next_node = self.add(
            l1.next if l1 else None,
            l2.next if l2 else None,
            carry
        )
        return ListNode(val, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)

# Time complexity: O(max(n, m)) where n and m are the lengths of the two lists
# Space complexity: O(max(n, m)) due to the recursive call stack and the new list created to store the sum of the two numbers