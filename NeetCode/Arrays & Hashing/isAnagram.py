class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map = {}

        for c in s:
            map[c] = map.get(c, 0) + 1
        
        for c in t:
            if c in map:
                map[c] -= 1
            else:
                return False
        
        for key in map:
            if map.get(key) != 0:
                return False
        
        return True
    
#Other solutions
#Sorting: we can sort both strings and compare them. If they are equal then they are anagrams.
#The time complexity of this solution is O(nlogn) because of the sorting step, and the space complexity is O(1) if we sort the strings in place, or O(n) if we create new sorted strings.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
#Hash Table: we can use a hash table to count the frequency of each character in the first string and then decrement the count for each character in the second string. If any count is not zero at the end, then they are not anagrams.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True