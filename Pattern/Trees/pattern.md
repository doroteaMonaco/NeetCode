# Trees — Patterns & Key Concepts

---

## 1. Core Traversals

### DFS — Recursive (most common)
```python
def dfs(node):
    if not node:
        return ...
    left  = dfs(node.left)
    right = dfs(node.right)
    # process node (post-order) or before recursing (pre-order)
    return ...
```
- **Pre-order** (root → left → right): serialization, building trees
- **In-order** (left → root → right): BST → sorted sequence
- **Post-order** (left → right → root): height, diameter, max path — compute children FIRST, then combine at parent

### BFS — Level-order with `deque`
```python
from collections import deque
q = deque([root])
while q:
    for _ in range(len(q)):   # freeze current level size
        node = q.popleft()
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
```
Use when: level-order traversal, right-side view, anything per-level.

---

## 2. Pattern: Post-order to Compute Global Maximum
Pass information **up** and maintain a global variable to track the best answer seen so far.

Used in: **Diameter of BT**, **Max Path Sum**, **Is Balanced**

```python
self.result = initial_value   # or use res = [initial_value]

def dfs(node):
    if not node:
        return base_case
    left  = dfs(node.left)
    right = dfs(node.right)
    self.result = max(self.result, left + right)  # update global at current node
    return 1 + max(left, right)                   # return only one direction upward
```

Key insight: the value **returned** up the tree (single path) differs from the value **recorded** globally (can span both children).

---

## 3. Pattern: Passing State Down the Tree
Pass extra context (bounds, max seen so far) as parameters to each call.

Used in: **Is Valid BST** (bounds), **Good Nodes** (max along path)

```python
def dfs(node, low, high):          # isValidBST
    if not node: return True
    if not (low < node.val < high): return False
    return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

def dfs(node, max_so_far):         # goodNodes
    if not node: return
    if node.val >= max_so_far:
        count += 1
    dfs(node.left,  max(max_so_far, node.val))
    dfs(node.right, max(max_so_far, node.val))
```

---

## 4. Pattern: BST Properties
In a BST, **in-order traversal produces a sorted sequence**.

| Property | How to use |
|---|---|
| Left subtree < root < Right subtree | Validate with bounds `(low, high)` |
| k-th smallest | In-order traversal, stop at k-th element |
| LCA | Navigate: both < root → go left; both > root → go right; else root is LCA |
| Search / insert | O(h) — compare and recurse one direction |

---

## 5. Pattern: Serialization / Deserialization
Pre-order DFS, use `"#"` as null marker and `","` as separator.

```python
# Serialize
def dfs(node):
    if not node: tree.append("#"); return
    tree.append(str(node.val))
    dfs(node.left); dfs(node.right)

# Deserialize
def build():
    val = next(it)
    if val == "#": return None
    node = TreeNode(int(val))
    node.left  = build()
    node.right = build()
    return node
```
Use a list + `",".join(...)` for O(n) string building (avoid `+=` on strings → O(n²)).

---

## 6. Pattern: Build Tree from Traversals
Given **preorder + inorder**, reconstruct the tree.

```
preorder[0]  → root
inorder      → find root index mid
              → inorder[:mid] = left subtree, inorder[mid+1:] = right subtree
```

Optimized: use a hashmap `{val: index}` on inorder to get `mid` in O(1), reducing total complexity from O(n²) to O(n).

---

## 7. Pattern: `nonlocal` vs Instance Variable vs List Wrapper
When you need to mutate a variable inside a nested function:

```python
# Option 1 — instance variable (class scope)
self.res = 0
def dfs(node): self.res += 1

# Option 2 — nonlocal (explicit declaration)
res = 0
def dfs(node):
    nonlocal res
    res += 1

# Option 3 — list wrapper (avoids nonlocal)
res = [0]
def dfs(node): res[0] += 1
```

---

## 8. Pattern: Iterative DFS with Explicit Stack
Replace call stack with an explicit stack to avoid recursion limits on very deep trees.

```python
stack = [root]
while stack:
    node = stack.pop()
    if not node: continue
    # process node
    stack.append(node.right)   # right first → left processed first (pre-order)
    stack.append(node.left)
```

For post-order iteratively, use a hashmap to memoize results per node (see diameterBT iterative solution).

---

## 9. Complexity Reference

| Scenario | Time | Space (recursion stack) |
|---|---|---|
| Balanced tree | O(n) | O(log n) |
| Skewed tree (worst case) | O(n) | O(n) |
| BST search/LCA | O(h) | O(h) |
| Build tree (naïve) | O(n²) | O(n) |
| Build tree (hashmap) | O(n) | O(n) |

---

## 10. Exercise → Pattern Map

| Exercise | Pattern |
|---|---|
| `invertBT` | Pre-order recursive DFS |
| `maxDepth` | Post-order DFS / BFS |
| `sameTrees` | Simultaneous DFS on two trees |
| `isSubTree` | DFS + same-tree check at each node |
| `isBalanced` | Post-order DFS returning height or -1 sentinel |
| `diameterBT` | Post-order DFS, global max = left + right height |
| `maxPath` | Post-order DFS, global max, only positive branches upward |
| `levelOrder` | BFS with level-size snapshot |
| `rightSideView` | BFS (last node per level) or right-first DFS |
| `goodNodes` | DFS passing max-so-far downward |
| `isValidBST` | DFS passing (low, high) bounds |
| `kthSmallest` | In-order DFS on BST |
| `LCA` (BST) | Iterative/recursive navigation using BST order |
| `buildTree` | Pre-order root + inorder split, hashmap for O(n) |
| `serialize` | Pre-order DFS with null markers |
