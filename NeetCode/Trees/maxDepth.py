
from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        h_left = self.maxDepth(root.left)
        h_right = self.maxDepth(root.right)

        return 1 + max(h_left, h_right)
# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)

#Other solutions
#Iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    
# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)

#BFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
    

# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)