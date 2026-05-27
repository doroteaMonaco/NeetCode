

from ast import List
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        for pair in points:
            x1, y1 = pair[0], pair[1]
            dist = math.sqrt((x1**2)+(y1**2))
            distances.append((dist, x1, y1))

        heapq.heapify(distances)
        res = [] * k 

        while k > 0:
            tup = heapq.heappop(distances)
            dist, x, y = tup
            res.append([x, y])
            k -= 1

        return res

#Time Complexity: O(n log n) due to the heap operations performed on the list of distances. The initial heapification takes O(n) time, and each of the k iterations involves popping the smallest element from the heap, which takes O(log n) time.
#Space Complexity: O(n) for the heap that stores the distances of all points from the origin. The space used by the result list is O(k), but since k is typically much smaller than n, the overall space complexity is dominated by O(n).

#Other solution
#Max Heap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        return res
    
#Time Complexity: O(n log k) due to the heap operations performed on the list of points. Each point is processed once, and adding an element to the heap takes O(log k) time. Since we maintain a heap of size at most k, the overall time complexity is O(n log k).
#Space Complexity: O(k) for the heap that stores the k closest points. The space used by the result list is also O(k), but since we are only storing k points, the overall space complexity is O(k).

#Other solution
#Quickselect
class Solution:
    def kClosest(self, points, k):
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]
    
#Time Complexity: O(n) on average for the quickselect algorithm, which is used to partition the points based on their distances from the origin. In the worst case, the time complexity can degrade to O(n^2) if the pivot selection consistently results in unbalanced partitions.
#Space Complexity: O(1) for the in-place partitioning of the points list, as we are not using any additional data structures to store the points. However, the recursive calls for partitioning can add to the space complexity, which in the worst case can be O(n) if the partitions are consistently unbalanced.