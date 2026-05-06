from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        temp = [0.0] * len(position)

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            temp[i] = (position[i], time)

        temp.sort(reverse=True)

        for p, t in temp:
            if stack and t <= stack[-1]:
                continue
            stack.append(t)
        
        return len(stack)
    
#Another solution using zip and list comprehension to create the temp list, which can be more concise and easier to read.
    
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        temp = [(p, s) for p, s in zip(position, speed)]
        temp.sort(reverse=True)

        for i in range(len(temp)):
            p, s = temp[i]
            time = (target - p) / s
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        
        return len(stack)
    


#Time complexity: O(n log n) where n is the number of cars. This is due to the sorting step, which dominates the overall time complexity. The rest of the operations (calculating time and iterating through the sorted list) are O(n).
#Space complexity: O(n) in the worst case when all cars form their own fleet, resulting in all time values being stored in the stack. In the best case when all cars form a single fleet, the space complexity is O(1) as only one time value will be stored in the stack.

#Other Solutions
#Sorting and Iteration
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets