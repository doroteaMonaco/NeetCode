

from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return 0

        h_left = self.dfs(root.left)
        h_right = self.dfs(root.right)

        if h_left == -1 or h_right == -1:
            return -1

        if abs(h_left - h_right) > 1:
            return -1

        return 1 + max(h_left, h_right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.dfs(root) != -1:
            return True
        return False

# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)

#Other solutions
#DFS with a tuple to store both balanced status and height
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 # Check if left and right subtrees are balanced and if their height difference is at most 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
    
# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)

#Iterative DFS
class Solution:
    def isBalanced(self, root):
        stack = []
        node = root
        last = None
        depths = {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right: # If the right child doesn't exist or has already been processed, we can process the current node
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    if abs(left - right) > 1:
                        return False

                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right

        return True
# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)