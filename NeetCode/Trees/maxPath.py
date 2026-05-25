from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.maxPath = - float('inf')

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            l = left if left > 0 else 0
            r = right if right > 0 else 0

            localSum = root.val + l + r

            self.maxPath = max(self.maxPath, localSum)

            return root.val + max(l, r)

        dfs(root)
        return self.maxPath
            
# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack

# Other solutions
#DFS with res as list to avoid nonlocal variable

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
    
# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack

