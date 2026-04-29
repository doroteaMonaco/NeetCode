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