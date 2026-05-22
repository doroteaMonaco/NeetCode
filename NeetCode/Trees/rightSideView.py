from collections import deque

from git import List
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        rightNodes = []

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            rightNodes.append(node.val)
        
        return rightNodes

# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to the queue storing nodes at each level

#Other solutions
#DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
    
# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to the queue storing nodes at each level
