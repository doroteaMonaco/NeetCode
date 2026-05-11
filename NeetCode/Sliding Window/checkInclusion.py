class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        need = len(count1)
        for i in range(len(s2)): # we are iterating through s2 with an index i, and for each index i, we are creating a new dictionary count2 to store the count of characters in the current window of s2 that we are checking against s1. We also have a variable cur to keep track of how many characters have the same count in both count1 and count2, and a variable need to keep track of how many unique characters are in s1. We then iterate through s2 starting from index i, and for each character in s2, we update the count of that character in count2 and check if it matches the count of the same character in count1. If it does, we increment cur. If the number of characters that have the same count in both dictionaries is equal to need, it means that we have found a permutation of s1 in s2, and we can return True. If we finish iterating through s2 without finding a permutation of s1, we return False.
            count2, cur = {}, 0
            for j in range(i, len(s2)): # we are iterating through s2 starting from the current index i, and for each character in s2, we are updating the count of that character in count2 and checking if it matches the count of the same character in count1. If it does, we increment the cur variable to keep track of how many characters have the same count in both dictionaries. If the number of characters that have the same count in both dictionaries is equal to the number of unique characters in s1, it means that we have found a permutation of s1 in s2, and we can return True.
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]: # if the count of the current character in count2 is greater than the count of the same character in count1, it means that we have found a character that has a higher count in count2 than in count1, and we can break out of the inner loop because we cannot have a permutation of s1 in s2 if there is a character that has a higher count in s2 than in s1.
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]: # if the count of the current character in count2 is equal to the count of the same character in count1, it means that we have found a character that has the same count in both count1 and count2, and we can increment the cur variable to keep track of how many characters have the same count in both dictionaries.
                    cur += 1
                if cur == need: # if the number of characters that have the same count in both count1 and count2 is equal to the number of unique characters in s1, it means that we have found a permutation of s1 in s2, and we can return True.
                    return True
        return False
    
# Time complexity: O(n * m) where n is the length of s2 and m is the length of s1. This is because we are iterating through s2 once, and for each character in s2, we are iterating through the remaining characters in s2 to check if they match the characters in s1, which takes O(m) time.  
# Space complexity: O(m) where m is the length of s1. This is because we are using a dictionary to store the count of characters in s1, and the size of the dictionary can be at most the length of s1.


# Other solution:
#Sliding window 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0) # we are iterating through the count arrays for s1 and s2, and for each character, we are checking if the count of that character in s1 is equal to the count of the same character in s2. If it is, we increment the matches variable to keep track of how many characters have the same count in both arrays. If the number of characters that have the same count in both arrays is equal to 26 (which is the total number of lowercase letters), it means that we have found a permutation of s1 in s2, and we can return True. If we finish iterating through the count arrays without finding a permutation of s1, we return False.

        l = 0
        for r in range(len(s1), len(s2)): 
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a') # we are calculating the index of the current character in s2 by subtracting the ASCII value of 'a' from the ASCII value of the current character. This gives us a number between 0 and 25, which corresponds to the index of that character in the count arrays for s1 and s2.
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]: # if the count of the current character in s2 is equal to the count of the same character in s1, it means that we have found a character that has the same count in both arrays, and we can increment the matches variable to keep track of how many characters have the same count in both arrays.
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: # if the count of the current character in s2 is equal to the count of the same character in s1 plus 1, it means that we have found a character that has a higher count in s2 than in s1, and we can decrement the matches variable to keep track of how many characters have the same count in both arrays.
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    
# Time complexity: O(n) where n is the length of s2. This is because we are iterating through s2 once with two pointers, which takes O(n) time.
# Space complexity: O(1) because we are using fixed-size arrays to store the count of characters in s1 and s2, and the size of the arrays is constant (26 for lowercase letters).