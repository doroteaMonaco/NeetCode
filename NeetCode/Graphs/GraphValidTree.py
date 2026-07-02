from collections import deque
from typing import List

#It is disconnected if the number of edges is not equal to n - 1, because a tree with n nodes must have n - 1 edges

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for v in adj[node]:
                if v == parent: #because we don't want to go back to the parent node, which would create a false positive for a cycle
                    continue
                if not dfs(v, node):
                    return False
            return True
        
        
        return dfs(0, -1) and len(visited) == n

#Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph
#Space complexity: O(V + E) for the graph and O(V) for the recursion

#Other solutions
#BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        q = deque()
        q.append((0, -1))
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for v in adj[node]:
                if v == parent:
                    continue
                if v in visited:
                    continue
                visited.add(v)
                q.append((v, node))

        
        return len(visited) == n

#Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph
#Space complexity: O(V + E) for the graph and O(V) for the queue

#Union Find

class DSU:
    def __init__(self, n):
        self.comps = n #number of components
        self.Parent = list(range(n + 1)) #parent of each node
        self.Size = [1] * (n + 1) #size of each component

    def find(self, node): #find the root of the component that node belongs to
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v): #union the components that u and v belong to, return False if they are already in the same component
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False

        self.comps -= 1
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1
    
#Time complexity: O(V + E*α(V)) where V is the number of vertices and E is the number of edges in the graph, α is the inverse Ackermann function
#Space complexity: O(V) for the DSU data structure