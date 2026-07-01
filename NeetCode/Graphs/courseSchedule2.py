from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            indegree[prereq] += 1 #compute the indegree of each course, which is the number of prerequisites for that course
            adj[course].append(prereq) #update the adjacency list to show that course depends on prereq
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish, output = 0, []
        while q:
            c = q.popleft()
            output.append(c)
            finish += 1
            for p in adj[c]:
                indegree[p] -= 1
                if indegree[p] == 0:
                    q.append(p)
        
        if finish != numCourses:
            return []
        return output[::-1]
    
#Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph
#Space complexity: O(V + E) for the graph and O(V) for the queue