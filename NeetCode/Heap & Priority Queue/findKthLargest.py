import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negNums = [-num for num in nums]
        heapq.heapify(negNums)
        kLargest = 0

        while k > 0:
            kLargest = -heapq.heappop(negNums)
            k -= 1
        
        return kLargest

#Time Complexity: O(n log n) due to the heap operations performed on the list of negative numbers. The initial heapification takes O(n) time, and each of the k iterations involves popping the smallest element from the heap, which takes O(log n) time.
#Space Complexity: O(n) for the heap that stores the negative numbers. The space used by the variable kLargest is O(1), so the overall space complexity is O(n).

#Other solution
#Sorting

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
#Time Complexity: O(n log n) due to the sorting operation performed on the list of numbers. Sorting takes O(n log n) time, and accessing the k-th largest element takes O(1) time.
#Space Complexity: O(1) if we ignore the space used by the sorting algorithm (assuming it is an in-place sorting algorithm). However, if the sorting algorithm used is not in-place, the space complexity would be O(n) due to the additional space required for the sorted list.

#Min Heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]
#Time Complexity: O(n log k) due to the heap operations performed on the list of numbers. Each number is processed once, and adding an element to the heap takes O(log k) time. Since we maintain a heap of size at most k, the overall time complexity is O(n log k).
#Space Complexity: O(k) for the heap that stores the k largest numbers. The space used by the variable that stores the k-th largest number is O(1), so the overall space complexity is O(k).

