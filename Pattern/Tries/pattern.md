# Tries Pattern

## When to use
- You need fast prefix search or prefix-based word lookup.
- The problem involves many words that share common prefixes.
- You need to implement a dictionary or autocomplete system.
- The search can include wildcards (like `.`) or multiple possible continuations.
- You need to efficiently prune search space during a board/backtracking search.

## Core idea
A trie (prefix tree) stores characters along a path from the root to a node. Each node represents a prefix. Leaf or terminal nodes mark the end of a valid word.

Common trie node structure:
- `children`: fixed-size array for `a-z` or dictionary/map for variable characters.
- `endWord` / `isWord` / `word`: marker that this node completes a word.

## Basic operations

### Insert
- Start at the root.
- For each character:
  - move to the child node for that character.
  - if missing, create the child node.
- mark the final node as a completed word.

### Search full word
- Traverse the trie character by character.
- If any child is missing, the word doesn't exist.
- At the end, return whether the current node is marked as a word.

### Prefix search
- Traverse the trie for every character in the prefix.
- If all nodes exist, the prefix is valid.
- You do not need to check the terminal word marker.

## Wildcard search pattern
- Use recursion/DFS when the query contains a wildcard like `.`.
- At a wildcard position, branch into every non-null child.
- Continue the search for the rest of the query from each child.
- If any branch reaches the end and is a terminal word, return true.

## Board search using trie + backtracking
- Build a trie from the given word list.
- For each cell in the board, start DFS if the first letter exists in trie root children.
- Pass the current trie node along with board coordinates.
- When you reach a node that marks a word, add it to results.
- Mark board cells as visited and restore them after recursive calls.
- Use trie node existence to prune invalid partial paths early.
- Deduplicate results using a set or by clearing the node's stored word after it is found.

## Implementation choices
- `children = [None] * 26` is best for lowercase English letters and constant-time access.
- `children = {}` is more flexible and can be simpler for sparse tries or non-latin alphabets.
- Storing `word` in a node lets you collect matched words directly during DFS.
- Storing a boolean `endWord` requires carrying the current prefix or path string separately.

## Complexity
- Insert/search/prefix: O(n), where `n` is the length of the input word or prefix.
- Space: O(T), where `T` is the total number of trie nodes created across all words.
- Word search on a board: roughly O(m * n * 4 * 3^(t-1) + s), where `m,n` are board dimensions, `t` is max word length, and `s` is total length of all words.

## Problem variants in this folder

### `PrefixTree.py`
- Classic trie implementation.
- Supports `insert(word)`, `search(word)`, and `startsWith(prefix)`.
- Good starter exercise for trie fundamentals.

### `wordDictionary.py`
- Adds wildcard search with `.`.
- Uses DFS over trie children when encountering a wildcard.
- Demonstrates combining trie traversal with recursion branching.

### `findWords.py`
- Builds a trie from a list of words.
- Uses board DFS + trie pruning to find all valid words on a letter grid.
- Demonstrates using a trie to speed up multi-word backtracking.

## Practical tips
- Always choose a trie when many strings share prefixes and you need prefix-based queries.
- Use backtracking with trie pruning for grid/board word search problems.
- For wildcard patterns, treat `.` as "match any child" and recursively explore all options.
- When adding words with duplicates, deduplicate results by clearing the matched word or using a set.
