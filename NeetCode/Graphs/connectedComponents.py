from collections import deque

from git import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        cc = 0

        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)
            for v in adj[node]:
                if v in visited:
                    continue
                if v == parent:
                    continue
                dfs(v, node)

        for i in range(n):
            if i not in visited:
                cc += 1
                dfs(i, -1)
        
        return cc

#Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph
#Space complexity: O(V + E) for the graph and O(V) for the recursion

#Other solutions
#BFS

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res
    
#Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph
#Space complexity: O(V + E) for the graph and O(V) for the queue