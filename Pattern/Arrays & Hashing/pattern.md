# Arrays & Hashing Patterns

## Main patterns

1. Hash maps / hash sets
   - Frequent pattern for counting occurrences or checking membership.
   - Used in `twoSum.py`, `isAnagram.py`, `anagramsGroups.py`, `containDuplicates.py`, `longestConsecutiveSequence.py`, `topKFrequent.py`, and `isValidSudoku.py`.
   - Examples:
     - store previous values or complements for `twoSum`
     - count character frequency for `isAnagram`
     - group words by character counts for `groupAnagrams`
     - detect duplicates with a set for `containDuplicates`
     - track numbers or frequencies for `longestConsecutive` and `topKFrequent`
     - keep row/column/box seen values for `isValidSudoku`

2. Sorting + two pointers
   - Alternative solution for problems where order helps find pairs or groups.
   - Found in `twoSum.py`, `isAnagram.py`, `anagramsGroups.py`, `longestConsecutiveSequence.py`, and `topKFrequent.py`.
   - Common use cases:
     - sort values and use two pointers to find target sums
     - sort strings to compare anagrams
     - sort words as keys for grouping anagrams
     - sort values to compute longest consecutive subsequences
     - sort frequency pairs to select top-k elements

3. Frequency bucket / bucket sort
   - Use a list of buckets indexed by count or frequency.
   - Used in `topKFrequent.py` to collect numbers by their occurrence counts and then traverse buckets from highest frequency.

4. Prefix / suffix accumulation
   - Build partial results from left and right, then combine.
   - Used in `productExceptSelf.py` with prefix and suffix product arrays to compute each result without division.

5. Encoded serialization
   - Store lengths or delimiters to safely encode variable-length strings.
   - Seen in `Encode&Decode.py` using either a size list + delimiter or `length#string` format for encoding and decoding string lists.

6. Matrix validation techniques
   - Check rows, columns, and sub-boxes independently.
   - In `isValidSudoku.py`, the main approach uses sets to verify no repeated digits in each row/column/3x3 box.
   - Advanced variant uses bit masks to reduce memory and speed up presence checks.

7. Sequence detection with sets
   - Convert array to a set to support O(1) membership checks.
   - `longestConsecutiveSequence.py` finds sequence starts and extends consecutive runs efficiently.

## Supporting complexity insights

- Many hash-based solutions aim for O(n) time with O(n) space.
- Sorting-based alternatives usually trade O(n log n) time for simpler logic.
- `productExceptSelf` uses O(n) time and O(n) extra space with prefix/suffix arrays.
- `Encode&Decode` operates in linear time relative to total string length.
- `isValidSudoku` can be implemented in O(1) space with bit masks and O(n^2) time for the 9x9 board.
