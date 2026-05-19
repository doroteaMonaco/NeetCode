
from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.diameter = max(self.diameter, left + right) # Update diameter if the path through the current node is larger

        return 1 + max(left, right) # Return the height of the current node

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        self.dfs(root)

        return self.diameter

# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)

#Other solutions
#Iterative DFS
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in mp: # If the left child exists and hasn't been processed yet, push it onto the stack
                stack.append(node.left)
            elif node.right and node.right not in mp: # If the right child exists and hasn't been processed yet, push it onto the stack
                stack.append(node.right)
            else:
                node = stack.pop()

                leftHeight, leftDiameter = mp[node.left] # Get the height and diameter of the left subtree
                rightHeight, rightDiameter = mp[node.right] # Get the height and diameter of the right subtree

                mp[node] = (1 + max(leftHeight, rightHeight),
                           max(leftHeight + rightHeight, leftDiameter, rightDiameter)) # Update the height and diameter for the current node

        return mp[root][1]

# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree)