from collections import deque
from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i : [] for i in range(numCourses)}

        for prereq, course in prerequisites:
            graph[prereq].append(course)

        visiting = set()

        def dfs(vertex: int):
            nonlocal visiting

            if vertex in visiting:
                return False
            
            if graph[vertex] == []:
                return True
            
            visiting.add(vertex)
            for pre in graph[vertex]:
                if not dfs(pre):
                    return False
            visiting.remove(vertex)
            graph[vertex] = [] #it is just an optimization to avoid visiting the same vertex again, since we already know it can be completed
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
#Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph
#Space complexity: O(V + E) for the graph and O(V) for the recursion

#Other solutions
#Kann's algorithm

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses #indegree[i] is the number of prerequisites for course i
        adj = [[] for i in range(numCourses)] #adj[i] is the list of courses that depend on course i
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses
    
#Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph  
#Space complexity: O(V + E) for the graph and O(V) for the queue
