from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], low: int, high: int) -> bool:
            if root is None:
                return True
            
            if not(low < root.val < high):
                return False

            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)

        return dfs(root, - float('inf'), float('inf'))

# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack

#Other solutions
#BFS
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True
    

# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to queue size