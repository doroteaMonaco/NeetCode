#Solution 1
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.times[key]
        left = 0
        right = len(timestamps) - 1
        index = -1

        while left <= right:
            m = (left + right) // 2
            if timestamps[m][0] > timestamp:
                right = m - 1
            elif timestamps[m][0] < timestamp:
                index = m
                left = m + 1
            else:
                return timestamps[m][1]

            if index != -1:
                return timestamps[index][1]
        
        return ""

# Time complexity: O(log(n)) where n is the number of timestamps for the given key. This is because we are performing a binary search on the list of timestamps, which takes O(log(n)) time.
# Space complexity: O(n) where n is the number of set operations performed. This is because we are storing the timestamps and values for each key in a list, and the size of the list can grow linearly with the number of set operations.

#Solution 2
from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1

        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        return ""

# Time complexity: O(log(n)) where n is the number of timestamps for the given key. This is because we are performing a binary search on the sorted dictionary of timestamps, which takes O(log(n)) time.
# Space complexity: O(n) where n is the number of set operations performed. This is because we are storing the timestamps and values for each key in a sorted dictionary, and the size of the dictionary can grow linearly with the number of set operations.

