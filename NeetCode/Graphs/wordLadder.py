from collections import defaultdict, deque

from git import List

#Create an hashmap of patterns to words, where a pattern is a word with one letter replaced by a wildcard character. For example, the word "hot" would have the patterns "*ot", "h*t", and "ho*". Then, we can use BFS to find the shortest path from the beginWord to the endWord, where each step in the path is a word that differs by one letter from the previous word.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        pattern = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                p = word[:j] + '*' + word[(j + 1):]
                pattern[p].append(word)
        
        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append(beginWord)
        numWords = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return numWords
                for j in range(len(word)):
                    p = word[:j] + '*' + word[(j + 1):]
                    for w in pattern[p]:
                        if w not in visited:
                            visited.add(w)
                            q.append(w)
            numWords += 1

        return 0
    
#Time complexity: O(N * M^2) where N is the number of words in the wordList and M is the length of each word. We are iterating through each word and for each word, we are iterating through each character to create a pattern. Then we are iterating through the list of words that match the pattern.
#Space complexity: O(N * M) for the pattern dictionary and O(N) for the visited set and the queue.

