
from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                node = TrieNode()
                curr.children[index] = node
            curr = curr.children[index]
        curr.endWord = True

    def searchDFS(self, root: Optional[TrieNode], word: str, index: int) -> bool:
        if index == len(word):
            return root.endWord
        
        char = word[index]
        
        if char == '.':
            for child in root.children:
                if child is not None:
                    if self.searchDFS(child, word, index + 1):
                        return True
            return False
        else:
            char_idx = ord(char) - ord('a')
            child = root.children[char_idx]
            if child is None:
                return False
            return self.searchDFS(child, word, index + 1)

    def search(self, word: str) -> bool:
        return self.searchDFS(self.root, word, 0)

#Time complexity: O(n) where n is the length of the word being searched
#Space complexity: O(t) where t is the total number of TrieNodes created in the Trie

#Other solution
#With hash map
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def searchDFS(self, root: Optional[TrieNode], word: str, index: int) -> bool:
        if index == len(word):
            return root.endOfWord
        
        char = word[index]
        
        if char == '.':
            for child in root.children.values():
                if self.searchDFS(child, word, index + 1):
                    return True
            return False
        else:
            if char not in root.children:
                return False
            child = root.children[char]
            return self.searchDFS(child, word, index + 1)

    def search(self, word: str) -> bool:
        return self.searchDFS(self.root, word, 0)
    
#Time complexity: O(n) where n is the length of the word being searched
#Space complexity: O(t) where t is the total number of TrieNodes created in the Trie