

import heapq

from git import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-stone for stone in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            stone1 = heapq.heappop(neg_stones)
            stone2 = heapq.heappop(neg_stones)

            if stone1 < stone2:
                diff = stone1 - stone2
                heapq.heappush(neg_stones, diff)
            
        return -neg_stones[0] if neg_stones else 0
    
#Time Complexity: O(n log n) due to the heap operations performed on the list of stones. The initial heapification takes O(n) time, and each of the n-1 iterations involves popping two elements and potentially pushing one element back onto the heap, which takes O(log n) time.
#Space Complexity: O(n) for the heap that stores the negative values of the stones.

#Other solution
#Bucketsort
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones: #Iterate through each stone in the input list and increment the corresponding index in the bucket array. The index represents the weight of the stone, and the value at that index represents how many stones of that weight are present. For example, if there are three stones of weight 5, then bucket[5] will be incremented three times, resulting in bucket[5] having a value of 3.
            bucket[stone] += 1

        first = second = maxStone #Initialize two variables, first and second, to keep track of the weights of the two heaviest stones. Both variables are initially set to maxStone, which is the maximum weight of any stone in the input list. This is done because we will be iterating through the bucket array from the heaviest weight downwards, and we want to start with the assumption that both first and second are at least as heavy as the heaviest stone.
        while first > 0:
            if bucket[first] % 2 == 0: #Check if the count of stones at the current weight (first) is even. If it is even, it means that all stones of that weight can be paired up and smashed together, resulting in no leftover stone of that weight. In this case, we can simply move on to the next lighter weight by decrementing first and continue the loop.
                first -= 1
                continue

            j = min(first - 1, second) #If the count of stones at the current weight (first) is odd, it means that there will be one leftover stone of that weight after pairing up as many stones as possible. In this case, we need to find the next heaviest stone (second) that can be smashed with the leftover stone of weight first. We set j to be the minimum of first - 1 and second because we want to find the next heaviest stone that is lighter than first but not heavier than second.
            while j > 0 and bucket[j] == 0:
                j -= 1

            if j == 0:
                return first
            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first