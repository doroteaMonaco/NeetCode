from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res
    
#Time complexity: O(n) because we iterate through the input list of strings and the encoded string, and we also iterate through the sizes list. The space complexity is O(n) because we store the sizes of the strings in a list and we also store the encoded string and the decoded list of strings.
#Other solutions
#Opttimal solution
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

#Time complexity: O(n) because we iterate through the input list of strings and the encoded string, and we also iterate through the sizes list. The space complexity is O(n) because we store the sizes of the strings in a list and we also store the encoded string and the decoded list of strings.