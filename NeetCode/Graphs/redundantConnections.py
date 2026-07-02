from git import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        cycleStart = -1
        cycle = set()

        def dfs(node, parent):
            nonlocal cycleStart
            if node in visited: #if it is already visited, then we have found a cycle
                cycleStart = node
                return True
            
            visited.add(node)
            for v in adj[node]:
                if v == parent:
                    continue
                if dfs(v, node): #if we found a cycle, then we need to add the current node to the cycle set
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart: #if we have reached the start of the cycle, then we can stop adding nodes to the cycle set
                        cycleStart = -1
                    return True
            return False
            

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle: #if both u and v are in the cycle, then this edge is the redundant connection
                return [u, v]
        
        return []

#Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph
#Space complexity: O(V + E) for the graph and O(V) for the recursion

#Other solutions
#Union-Find
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
#Time complexity: O(V + E*α(V)) where V is the number of vertices and E is the number of edges in the graph, and α is the inverse Ackermann function
#Space complexity: O(V) for the parent and rank arrays
