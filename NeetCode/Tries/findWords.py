from git import List, Optional


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = ""

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                node = TrieNode()
                curr.children[index] = node
            curr = curr.children[index]
        curr.word = word

class Solution:
    def dfs(self, r: int, c: int, node: Optional[TrieNode]):
        if node.word != "":
            self.res.add(node.word)
            node.word = ""

        char = self.board[r][c]
        self.board[r][c] = "#"

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.lenRow and 0 <= nc < self.lenCol and self.board[nr][nc] != "#":
                ch = self.board[nr][nc]
                index = ord(ch) - ord('a')
                if node.children[index] is not None:
                    self.dfs(nr, nc, node.children[index])
        self.board[r][c] = char
        

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for string in words:
            root.addWord(string)

        self.res = set()
        self.board = board
        self.lenRow, self.lenCol = len(board), len(board[0])
        r, c = 0, 0

        for r in range(self.lenRow):
            for c in range(self.lenCol):
                char = self.board[r][c]
                index = ord(char) - ord('a')
                if root.children[index] is not None:
                    self.dfs(r, c, root.children[index])
                    
        return list(self.res)
        
#Time complexity: O(m∗n∗4∗3t−1+s) 
#Where m is the number of rows, n is the number of columns, t is the maximum length of any word in the array 
#words and s is the sum of the lengths of all the words.
#Space complexity: O(s) where s is the sum of the lengths of all the words in the array words

#Other solution
#With hash map
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
    

#Time complexity: O(m∗n∗4∗3t−1+s) 
#Where m is the number of rows, n is the number of columns, t is the maximum length of any word in the array 
#words and s is the sum of the lengths of all the words.
#Space complexity: O(s) where s is the sum of the lengths of all the words in the array words