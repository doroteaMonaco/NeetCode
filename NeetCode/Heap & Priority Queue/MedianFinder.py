import heapq


class MedianFinder:

    def __init__(self):
       self.minHeap = []
       self.maxHeap = [] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        maxValue = heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, -maxValue)
        if len(self.minHeap) - len(self.maxHeap) >= 2:
            minValue = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -minValue)

    def findMedian(self) -> float:
        median = 0
        if len(self.minHeap) == len(self.maxHeap):
            m1 = self.minHeap[0]
            m2 = -self.maxHeap[0]
            median = (m1 + m2) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            median = self.minHeap[0]
        else:
            median = -self.maxHeap[0]

        return median
    
#Time Complexity: O(log n) for addNum where n is the number of elements in the data structure, and O(1) for findMedian. The addNum method involves heap operations which take O(log n) time, while findMedian simply retrieves the top elements from the heaps which takes O(1) time.
#Space Complexity: O(n) where n is the number of elements in the data structure.


