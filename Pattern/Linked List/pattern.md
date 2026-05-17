# Linked List — Patterns

## 1. Fast & Slow Pointers (Floyd's Tortoise and Hare)
Move one pointer one step at a time and another two steps at a time.

- **Detect cycle** — if they meet, a cycle exists (`hasCycle.py`)
- **Find middle** — when `fast` reaches the end, `slow` is at the midpoint (`reorderList.py`)
- **Find cycle entrance** — after meeting, reset one pointer to start; the new meeting point is the cycle entrance (`findDuplicate.py`)

```python
slow, fast = head, head.next
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

---

## 2. Dummy Node
Prepend a sentinel node to avoid special-casing the head. Return `dummy.next` at the end.

- Useful when the head itself may be removed or replaced (`removeNthNodeFromEnd.py`, `reverseKgroups.py`, `mergeTwoSortedLists.py`)

```python
dummy = ListNode(0, head)
# ... manipulate list ...
return dummy.next
```

---

## 3. Two Pointers with Fixed Gap
Start `fast` n steps ahead of `slow`; when `fast` reaches the end, `slow` points to the target node.

- **Remove nth node from end** — gap of n between fast and slow (`removeNthNodeFromEnd.py`)

```python
for _ in range(n):
    fast = fast.next
while fast.next:
    fast = fast.next
    slow = slow.next
slow.next = slow.next.next
```

---

## 4. In-Place Reversal
Reverse pointer direction iteratively by maintaining `prev` and `curr`.

- **Full list reversal** (`reverseList.py`)
- **Reverse second half only** (`reorderList.py`)
- **Reverse in k-group segments** (`reverseKgroups.py`)

```python
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
```

---

## 5. Merge Two Sorted Lists
Use a dummy head and advance whichever pointer holds the smaller value.

- **Merge two lists** (`mergeTwoSortedLists.py`)
- **Used as a subroutine in merge-k** (`mergeKLists.py`)

---

## 6. Divide and Conquer on Lists
Repeatedly merge pairs of lists, halving the problem size each round — O(n log k).

- **Merge k sorted lists** (`mergeKLists.py`)

```python
while len(lists) > 1:
    merged = []
    for i in range(0, len(lists), 2):
        merged.append(merge2(lists[i], lists[i+1] if i+1 < len(lists) else None))
    lists = merged
```

---

## 7. Hash Map for Node Cloning / Visited Tracking
Map original nodes to their copies to wire `next` and `random` pointers in a second pass.

- **Deep copy with random pointers** (`copyRandomList.py`)
- **Cycle detection (alternative O(n) space)** (`hasCycle.py`)

```python
old_to_new = {}
cur = head
while cur:
    old_to_new[cur] = Node(cur.val)
    cur = cur.next
# second pass: set .next and .random
```

---

## 8. Doubly Linked List + Hash Map (LRU Cache)
Combine a doubly linked list (to maintain access order in O(1)) with a hash map (for O(1) lookup).

- Most-recently-used node sits at the tail; least-recently-used sits at the head.
- On access/update: remove node from current position, re-insert at tail.
- On eviction: remove head's neighbour.
- (`LRUCache.py`)

---

## 9. Simultaneous Traversal with Carry
Walk two lists in parallel, computing digit-by-digit results and propagating carry.

- **Add two numbers** (`addTwoNumber.py`)

```python
while l1 or l2 or carry:
    total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
    carry, digit = divmod(total, 10)
```

---

## 10. Recursive Approach
Solve the subproblem on the tail and wire the current node on the way back up.

- **Reverse list recursively** (`reverseList.py`)
- **Add two numbers recursively** (`addTwoNumber.py`)
- **Copy random list recursively with memoisation** (`copyRandomList.py`)

---

## 11. Array-as-Linked-List (Floyd's on Array)
Treat array values as `next` pointers: `nums[i]` points to index `nums[i]`. Apply Floyd's cycle detection to find the duplicate.

- **Find duplicate number** (`findDuplicate.py`)

---

## Quick Reference

| Problem | Primary Pattern |
|---|---|
| `reverseList` | In-Place Reversal, Recursion |
| `hasCycle` | Fast & Slow Pointers |
| `mergeTwoSortedLists` | Dummy Node, Merge |
| `reorderList` | Fast & Slow (find middle) + In-Place Reversal + Merge |
| `removeNthNodeFromEnd` | Dummy Node + Two Pointers with Fixed Gap |
| `reverseKgroups` | Dummy Node + In-Place Reversal (segments) |
| `mergeKLists` | Divide and Conquer + Merge |
| `addTwoNumber` | Simultaneous Traversal + Carry |
| `copyRandomList` | Hash Map for Cloning |
| `findDuplicate` | Array-as-Linked-List + Floyd's Cycle |
| `LRUCache` | Doubly Linked List + Hash Map |
