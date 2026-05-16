


from matplotlib import collections
from pyparsing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
            
        corr_map = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            corr_map[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = corr_map[curr]
            copy.next = corr_map.get(curr.next)
            copy.random = corr_map.get(curr.random)
            curr = curr.next

        return corr_map[head]


# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(n) due to the dictionary storing the mapping of original nodes to their copies

#Other solutions
#recursion
class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head in self.map:
            return self.map[head]

        copy = Node(head.val)
        self.map[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.map.get(head.random)
        return copy
    
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(n) due to the dictionary storing the mapping of original nodes to their copies and the recursive call stack

#Hash map one pass
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        cur = head
        while cur:
            oldToCopy[cur].val = cur.val
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
    
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(n) due to the dictionary storing the mapping of original nodes to their copies

#Space optimized solution

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        l1 = head
        while l1 is not None: # for each node in the original list, create a copy and insert it right after the original node
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next

        newHead = head.next

        l1 = head
        while l1 is not None: # set the random pointers of the copied nodes
            if l1.random is not None:
                l1.next.random = l1.random.next
            l1 = l1.next.next

        l1 = head
        while l1 is not None: # restore the original list and separate the copied list
            l2 = l1.next
            l1.next = l2.next
            if l2.next is not None:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead
    
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(1) since we are not using any additional data structures to store the mapping of original nodes to their copies, and we are modifying the original list in place to create the copied list.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        l1 = head
        while l1: # for each node in the original list, create a copy and insert it right after the original node
            l2 = Node(l1.val)
            l2.next = l1.random # store the random pointer of the original node in the next pointer of the copied node
            l1.random = l2 # point the random pointer of the original node to the copied node
            l1 = l1.next # move to the next original node

        newHead = head.random # the head of the copied list is the random pointer of the original head

        l1 = head
        while l1: # set the random pointers of the copied nodes
            l2 = l1.random # the copied node is the random pointer of the original node
            l2.random = l2.next.random if l2.next else None # set the random pointer of the copied node to the random pointer of the original node's next node
            l1 = l1.next 

        l1 = head
        while l1 is not None: # restore the original list and separate the copied list
            l2 = l1.random # the copied node is the random pointer of the original node
            l1.random = l2.next if l2.next else None # restore the random pointer of the original node to its original value
            l2.next = l1.next.random if l1.next else None # set the next pointer of the copied node to the next copied node
            l1 = l1.next

        return newHead
    
# Time complexity: O(n) where n is the number of nodes in the linked list
# Space complexity: O(1) since we are not using any additional data structures to store the mapping of original nodes to their copies, and we are modifying the original list in place to create the copied list.       




