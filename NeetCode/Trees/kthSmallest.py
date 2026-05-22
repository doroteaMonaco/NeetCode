from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def dfs_inorder(root: Optional[TreeNode]):
            if not root:
                return

            dfs_inorder(root.left)
            inorder.append(root.val)
            dfs_inorder(root.right)
        
        dfs_inorder(root)

        return inorder[k - 1]
    
# Time complexity: O(n) where n is the number of nodes in the treee
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack and the inorder list storing all node values

#Other solutions
#Recursive DFS with early stopping
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            if not node:
                return

            dfs(node.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res
    
# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack