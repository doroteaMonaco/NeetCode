from typing import List

#Bucket Sort: we can use a bucket sort approach, where we create a list of buckets, where the index of the bucket represents the frequency of the numbers in the input array. We then iterate through the input array and add each number to the corresponding bucket based on its frequency. Finally, we iterate through the buckets in reverse order and add the numbers to the result list until we have k elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for i in range(len(nums) + 1)] #List of lists, where the index represents the frequency and the value is a list of numbers that have that frequency.
        res = []

        for num in nums:
            map[num] = 1 + map.get(num, 0) #if the number is not in the map, we initialize its frequency to 1, otherwise we increment its frequency by 1.

        for num, f in map.items():
            freq[f].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                

#Time complexity: O(n) because we iterate through the input array and the frequency map, and we also iterate through the buckets in reverse order. The space complexity is O(n) because we store the frequency of each number in the map and we also store the numbers in the buckets.
#Others solutions

#Min-Heap: after counting the frequency of each number, we can use a min-heap to keep track of the top k frequent numbers. We iterate through the frequency map and add each number to the min-heap. If the size of the min-heap exceeds k, we remove the least frequent number from the heap. Finally, we return the numbers in the min-heap as the result.
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
    
#Time complexity: O(n log k) because we iterate through the frequency map and add each number to the min-heap, which takes O(log k) time. The space complexity is O(n) because we store the frequency of each number in the map and we also store the numbers in the min-heap.

#Sorting: we can sort the frequency map by frequency and return the top k elements. The time complexity of this solution is O(n log n) because of the sorting step, and the space complexity is O(n) because we store the frequency of each number in the map.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res