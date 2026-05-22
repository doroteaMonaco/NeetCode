
from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxNode = - float('inf')
        goodNodes = 0
        
        def dfs(root: Optional[TreeNode], maxNode: int):
            nonlocal goodNodes #to modify the variable declared in the outer scope
            if root is None:
                return
            
            if root.val >= maxNode:
                maxNode = max(maxNode, root.val)
                goodNodes += 1
            
            dfs(root.left, maxNode)
            dfs(root.right, maxNode)
        
        dfs(root, maxNode)
        return goodNodes
    
# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack

#Other solutions
#BFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque()

        q.append((root,-float('inf')))

        while q:
            node,maxval = q.popleft()
            if node.val >= maxval:
                res += 1

            if node.left:
                q.append((node.left,max(maxval,node.val)))

            if node.right:
                q.append((node.right,max(maxval,node.val)))

        return res
    

# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to the queue storing nodes at each level