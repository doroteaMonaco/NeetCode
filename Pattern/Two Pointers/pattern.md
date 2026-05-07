# Two Pointers Patterns

## Main patterns

1. Converging two pointers (left & right)
   - Place one pointer at the start and one at the end; move them toward each other based on a comparison condition.
   - Used in `IsPalindrome.py`, `maxArea.py`, `trapWater.py`, and `twoSum.py`.
   - Examples:
     - compare characters from both ends to verify a palindrome in `IsPalindrome`
     - maximize container area by always moving the pointer with the smaller height inward in `maxArea`
     - track the current max height on both sides; advance the side with the smaller max and accumulate trapped water in `trapWater`
     - find a pair summing to a target in a sorted array by narrowing the window in `twoSum`

2. Sort + two pointers
   - Sort the array first, then fix one element with an outer loop and use two pointers on the remaining subarray.
   - Used in `3sum.py` and `twoSum.py`.
   - Examples:
     - fix element `a`, then use left/right pointers to find pairs summing to `-a` in `3sum`; skip duplicates after sorting to avoid repeated triplets
     - binary-search variant in `twoSum` uses a sorted array and narrows the search window for each fixed element

3. Prefix / suffix max tracking
   - Precompute or maintain running maximums from the left and right to answer range queries in O(1) per element.
   - Used in `trapWater.py` (prefix/suffix arrays variant): fill `leftMax` and `rightMax` arrays, then compute water at each index as `min(leftMax[i], rightMax[i]) - height[i]`.

4. Input preprocessing before two pointers
   - Filter or normalize the input string/array before applying pointer logic.
   - Used in `IsPalindrome.py`: strip non-alphanumeric characters and lowercase the string, then run the converging pointer check on the cleaned version.

5. Duplicate skipping
   - After finding a valid answer, advance pointers past all identical values to avoid emitting duplicate results.
   - Used in `3sum.py`: skip duplicate values of the outer element and of the left pointer after recording each triplet.

## Supporting complexity insights

- Converging two-pointer solutions are O(n) time and O(1) extra space (ignoring output).
- `3sum` is O(n²) because of the outer loop combined with the inner two-pointer scan; sorting adds O(n log n) but is dominated by O(n²).
- `twoSum` (two-pointer on a sorted array) is O(n) time and O(1) space; the binary-search variant is O(n log n) time and O(1) space.
- The prefix/suffix arrays approach in `trapWater` trades O(n) extra space for a simpler implementation; the two-pointer approach achieves the same O(n) time with O(1) space.
- `IsPalindrome` is O(n) time and O(n) space due to building the cleaned string; using in-place pointer checks on the original string would reduce space to O(1).
