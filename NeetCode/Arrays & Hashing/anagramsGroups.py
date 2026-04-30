from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list) #We use a defaultdict to store the anagrams, where the key is a tuple representing the count of each character in the word, and the value is a list of words that have the same character count (i.e., are anagrams of each other).

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            map[tuple(count)].append(word) #We convert the count list to a tuple so that it can be used as a key in the hash map. We then append the original word to the list of anagrams corresponding to that character count.
        
        return list(map.values()) #Finally, we return the values of the hash map, which are the lists of anagrams.
    
#This solution has a time complexity of O(n * k), where n is the number of words in the input list and k is the maximum length of a word. This is because we iterate through each word and count the characters, which takes O(k) time. The space complexity is also O(n * k) in the worst case, if all words are anagrams of each other.

#Other solutions
#Sorting: we can sort each word and use the sorted word as a key in the hash map. The time complexity of this solution is O(n * k log k) because of the sorting step, and the space complexity is O(n * k) in the worst case if all words are anagrams of each other.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())