
from collections import deque

from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = [] #Le stringhe sono immutabili quindi è meglio usare una lista e poi unirla alla fine, altrimenti avremmo O(n^2) a causa della concatenazione delle stringhe

        def dfs(root: Optional[TreeNode]):
            if root is None:
                tree.append("#") 
                return

            tree.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return ",".join(tree) #Separatore per distinguere i nodi, altrimenti avremmo problemi con numeri a più cifre
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = iter(data.split(','))

        def build_tree():
            node = next(tree)
            if node == "#":
                return None

            root = TreeNode(int(node))

            root.left = build_tree()
            root.right = build_tree()

            return root

        return build_tree()

# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to recursion stack and the list used for serialization

# Other solutions
#BFS
class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index += 1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index += 1
        return root
    
# Time complexity: O(n) where n is the number of nodes in the tree
# Space complexity: O(n) in worst case (skewed tree), O(log n) in best case (balanced tree) due to the queue used for BFS and the list used for serialization