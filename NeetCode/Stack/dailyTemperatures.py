from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackI, stackT = stack.pop()
                res[stackI] = i - stackI
            stack.append((i, t))
        return res

#Time complexity: O(n) where n is the number of temperatures in the input list. Each temperature is processed once, and each index is pushed and popped from the stack at most once.
#Space complexity: O(n) in the worst case when the temperatures are in decreasing order, resulting in all indices being pushed onto the stack. In the best case when the temperatures are in increasing order, the space complexity is O(1) as the stack will only contain one index at a time.

#Other Solutions
#Dynamic Programming
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1 # Start with the next day
            while j < n and temperatures[j] <= temperatures[i]: # If the next day's temperature is not warmer, jump to the day after that using the previously computed result
                if res[j] == 0: # If there are no warmer days ahead, break the loop
                    j = n 
                    break
                j += res[j] # Jump to the next warmer day using the previously computed result

            if j < n: # If a warmer day is found, calculate the difference in days      
                res[i] = j - i
        return res
    
#If the j temperature is not warmer than the current temperature, we can jump to the next warmer day using the previously computed result in res[j]. This allows us to skip over indices that we know will not yield a warmer temperature, thus optimizing the search for the next warmer day.
#Otherwise if res[j] is 0, it means there are no warmer days ahead for that index, and we can break the loop to avoid unnecessary checks.
#Time complexity: O(n) where n is the number of temperatures in the input list. Each temperature is processed once, and the inner while loop jumps over indices based on previously computed results, ensuring that each index is visited at most once.
#Space complexity: O(n) for the result list that stores the number of days until a warmer temperature for each day. The space used for the result list is proportional to the number of temperatures in the input list.