class ListNode:
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # dictionary to store the key-node pairs for O(1) access
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail # initialize the head and tail of the doubly linked list
        self.tail.prev = self.head # initialize the head and tail of the doubly linked list

    def remove(self, node):
        prec = node.prev
        nxt = node.next
        prec.next = nxt
        nxt.prev = prec

    def insert(self, node):
        prev = self.tail.prev
        nxt = self.tail
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key]) # remove the node from its current position
            self.insert(self.map[key]) # insert the node at the tail (most recently used)
            return self.map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key]) # remove the node from its current position
        self.map[key] = ListNode(key, value)
        self.insert(self.map[key]) # insert the node at the tail (most recently used)

        if len(self.map) > self.capacity:
            lru = self.head.next
            self.remove(lru) # remove the least recently used node
            del self.map[lru.key] # delete the least recently used node from the map


# Time complexity: O(1) for both get and put operations
# Space complexity: O(capacity) due to the map storing the key-node pairs and the doubly linked list storing the nodes up to the capacity of the cache          
#the most recently used node is always at the tail of the doubly linked list, while the least recently used node is always at the head of the doubly linked list. When a node is accessed or updated, it is moved to the tail of the list to indicate that it is the most recently used. When the cache exceeds its capacity, the node at the head of the list (the least recently used) is removed from both the list and the map.


# Other solutions: using an OrderedDict from the collections module to maintain the order of access and simplify the implementation of the LRU cache. The OrderedDict allows us to move a key to the end of the dictionary when it is accessed or updated, and it also provides a method to pop the least recently used item when the cache exceeds its capacity.
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) # move the accessed key to the end to show that it was recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key) # move the updated key to the end to show that it was recently used
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False) # pop the first item (least recently used) from the cache when the capacity is exceeded

# Time complexity: O(1) for both get and put operations
# Space complexity: O(capacity) due to the OrderedDict storing the key-value pairs up to the capacity of the cache