from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:   

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if root.val == subRoot.val:
            left = self.isSameTree(root.left, subRoot.left)
            right = self.isSameTree(root.right, subRoot.right)
            return left and right

        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
# Time complexity: O(m * n) where m is the number of nodes in the main tree and n is the number of nodes in the subtree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack  

#Other solutions