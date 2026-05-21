

from git import List
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfsByLevel(self, root: Optional[TreeNode], level: int, res: List[List[int]]):
        if root is None:
            return
        
        if len(res) <= level:
            res.append([])

        res[level].append(root.val)

        self.dfsByLevel(root.left, level + 1, res)
        self.dfsByLevel(root.right, level + 1, res)



    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        treeByLevels = []

        self.dfsByLevel(root, 0, treeByLevels)
        return treeByLevels


# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack  

#Other solutions
#BFS
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res
    
# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to queue size

