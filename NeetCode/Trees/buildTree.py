

from ast import List
from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                mid = i
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
    
# Time complexity: O(n^2) in worst case (skewed tree), O(n log n) in best case (balanced tree)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack

# Other solutions
#Hash Map and DFS
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
    

# Time complexity: O(n)
# Space complexity: O(n) due to the hash map and recursion stack in worst case (skewed tree), O(log n) in best case (balanced tree)

#DFS with limit
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))
    
# Time complexity: O(n)
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack

#Morris Traversal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head # Start with a dummy node to simplify edge cases
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right = curr.right) # Create a new node with the current value from preorder and set it as the right child of the current node
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr) # Create a new node with the current value from preorder and set it as the left child of the current node
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]: # If the right child of the current node exists and matches the current value in inorder, move to the right child and increment j
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

        return head.right
    
# Time complexity: O(n)
# Space complexity: O(1) since we are modifying the tree in place and not using any additional data structures, but the recursion stack can go up to O(n) in worst case (skewed tree) and O(log n) in best case (balanced tree)