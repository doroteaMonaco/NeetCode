from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:  

    def Merge2Lists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(0)
        curr = merged

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
                curr = curr.next
            else:
                curr.next = head2
                head2 = head2.next
                curr = curr.next

        while head1:
            curr.next = head1
            head1 = head1.next
            curr = curr.next
        while head2:
            curr.next = head2
            head2 = head2.next
            curr = curr.next
        
        return merged.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                head1 = lists[i]

                if i + 1 < len(lists):
                    head2 = lists[i + 1]
                    result = self.Merge2Lists(head1, head2)
                else:
                    result = head1

                merged.append(result)
            lists = merged

        return lists[0]

# Time complexity: O(n log k) where n is the total number of nodes across all lists and k is the number of lists
# Space complexity: O(1) if we don't consider the space used by the output list

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])

        return lists[-1]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
    
# Time complexity: O(k * n) where k is the number of lists and n is the total number of nodes across all lists
# Space complexity: O(1) if we don't consider the space used by the output list


#Heap approach: we can use a min-heap to keep track of the smallest node among the heads of the k lists. We can repeatedly extract the minimum node from the heap and add it to the merged list, and then add the next node from the same list to the heap. This approach has a time complexity of O(n log k) where n is the total number of nodes across all lists and k is the number of lists, and a space complexity of O(k) due to the heap.
from typing import List, Optional
import heapq
class NodeWrapper: # a wrapper class to compare the nodes in the min-heap based on their values
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode(0)
        cur = res
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst)) # push the head of each list into the min-heap

        while minHeap: # while the min-heap is not empty
            node_wrapper = heapq.heappop(minHeap) # pop the smallest node from the min-heap
            cur.next = node_wrapper.node
            cur = cur.next

            if node_wrapper.node.next: # if the popped node has a next node, push it into the min-heap
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next)) # push the next node of the popped node into the min-heap

        return res.next