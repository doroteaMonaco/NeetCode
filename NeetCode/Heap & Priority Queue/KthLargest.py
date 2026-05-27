import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap) #Rearrange the elements in the list to satisfy the heap property
        while len(self.minHeap) > k: #If the number of elements in the min-heap exceeds k, we remove the smallest element (the root of the heap) until we have at most k elements left. This ensures that the min-heap always contains the k largest elements seen so far.
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #Add a new value to the min-heap. This operation maintains the heap property, ensuring that the smallest element is always at the root of the heap.
        if len(self.minHeap) > self.k: #If the number of elements in the min-heap exceeds k after adding the new value, we remove the smallest element (the root of the heap) to maintain only the k largest elements in the min-heap.
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


#Time Complexity: O(log k) for the add method, where k is the number of elements in the min-heap. This is because adding an element to the heap and maintaining the heap property takes logarithmic time relative to the number of elements in the heap. The constructor has a time complexity of O(n log n) due to heapifying the initial list and potentially removing elements until only k remain.
#Space Complexity: O(k) for the min-heap, as it will store at most k elements at any time. The space used by the constructor is O(n) due to the initial list of numbers, but this is not additional space since it is provided as input.
