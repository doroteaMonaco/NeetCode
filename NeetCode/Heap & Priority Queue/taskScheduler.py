from collections import deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            if task in freq:
                freq[task] += 1
            else:
                freq[task] = 1
        
        taskfreq = [-f for f in freq.values()]
        heapq.heapify(taskfreq)

        waitQueue = deque()
        time = 0

        while taskfreq or waitQueue:
            time += 1

            if taskfreq:
                task = heapq.heappop(taskfreq) + 1
                if task < 0:
                    waitQueue.append([task, time + n])
            
            if waitQueue:
                if waitQueue[0][1] == time:
                    task = waitQueue.popleft()[0]
                    heapq.heappush(taskfreq, task)

        return time

#Time Complexity: O(n log k) where n is the number of tasks and k is the number of unique tasks. The heap operations take O(log k) time, and we perform these operations for each task.
#Space Complexity: O(k) for the heap that stores the frequencies of the unique tasks and the wait queue that stores the tasks that are waiting to be executed. The space used by the frequency dictionary is also O(k), so the overall space complexity is O(k).

#Other solution
#Greedy
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        count.sort()
        maxf = count[25] #the maximum frequency of any task
        idle = (maxf - 1) * n #the number of idle slots needed to separate the most frequent tasks

        for i in range(24, -1, -1):
            idle -= min(maxf - 1, count[i])
        return max(0, idle) + len(tasks)

#Time Complexity: O(n) to count the frequency of tasks and O(1) to sort the fixed-size count array. The overall time complexity is O(n).
#Space Complexity: O(1) since the count array has a fixed size of 26, regardless of the number of tasks. The space used by the frequency count is constant, so the overall space complexity is O(1).

#Math
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0 # Count the number of tasks with the maximum frequency

        time = (maxf - 1) * (n + 1) + maxCount # Calculate the minimum time required to execute all tasks
        return max(len(tasks), time)
    
#Time Complexity: O(n) to count the frequency of tasks and O(1) to find the maximum frequency and count the number of tasks with that frequency. The overall time complexity is O(n).
#Space Complexity: O(1) since the count array has a fixed size of 26

