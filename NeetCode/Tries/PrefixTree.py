class TrieNode:
    def __init__(self):
        self.children = 26 * [None]
        self.endWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                node = TrieNode()
                curr.children[index] = node
            curr = curr.children[index]
        curr.endWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.endWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True
        

#Time complexity O(n)
#Space complexity: O(t)
#Where n is the length of the string and t is the total number of TrieNodes created in the Trie

#Prefix Tree with hash map

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
#Time complexity O(n)
#Space complexity: O(t)
#Where n is the length of the string and t is the total number of TrieNodes created in the Trie
