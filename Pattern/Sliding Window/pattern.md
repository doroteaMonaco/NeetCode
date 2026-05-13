# Sliding Window Pattern

## Overview
The Sliding Window technique uses two pointers (left and right) to create a "window" of elements that moves across the input. This pattern is ideal for problems involving **contiguous subarrays or substrings**.

## Major Patterns

### 1. **Two Pointers (Left and Right)**
- **Description**: Maintain two pointers defining the window boundaries
- **Usage**: Expand and contract the window to solve the problem
- **Time Complexity**: O(n) - each pointer moves through the array at most once
- **Examples**: 
  - `maxSlidingWindow.py` - track window of size k
  - `lengthOfLongestSubstring.py` - find longest substring without duplicates
  - `minWindow.py` - find minimum window containing all characters
  - `maxProfit.py` - find best buy/sell pair

```python
left = 0
for right in range(len(array)):
    # Expand window with right pointer
    # ... add/process array[right]
    
    # Shrink window when condition violated
    while condition_violated:
        # ... remove/process array[left]
        left += 1
```

### 2. **Window Expansion**
- **Description**: Move the right pointer to expand the window and include new elements
- **When to use**: Always start by expanding the window
- **Key action**: Add element at `right` to the window's data structure
- **Examples**:
  - `lengthOfLongestSubstring.py` - add character to set
  - `minWindow.py` - add character to window map
  - `characterReplacement.py` - count character frequency

### 3. **Window Shrinking**
- **Description**: Move the left pointer to shrink the window when a constraint is violated
- **When to use**: 
  - Window becomes invalid (duplicate found, condition exceeded, etc.)
  - Need to find minimum window size
- **Key action**: Remove element at `left` from the window's data structure
- **Examples**:
  - `lengthOfLongestSubstring.py` - remove duplicate until valid
  - `minWindow.py` - shrink until needed characters count drops
  - `characterReplacement.py` - shrink until replacements ≤ k

```python
while condition_violated:
    # Remove from window
    # Process array[left]
    left += 1
```

### 4. **Character Frequency Tracking**
- **Description**: Use hash map/dictionary to count character occurrences in the window
- **Data Structures**:
  - `Dictionary/HashMap`: For arbitrary character sets
  - `Array[26]`: For lowercase letters only (more efficient)
  - `Set`: When only checking existence, not frequency
- **Examples**:
  - `lengthOfLongestSubstring.py` - track unique characters
  - `minWindow.py` - compare character counts with target
  - `characterReplacement.py` - track most frequent character
  - `checkInclusion.py` - verify permutation matches

```python
charMap = {}
charMap[char] = charMap.get(char, 0) + 1  # Add
charMap[char] -= 1  # Remove
```

### 5. **Valid Window Condition**
- **Description**: Check if the current window satisfies the problem's constraints
- **Patterns**:
  - **Character Matching**: All required characters in window with correct counts
  - **Threshold Check**: Property (max char count, window size, etc.) within limits
  - **Uniqueness**: No duplicate characters in window
- **Examples**:
  - `minWindow.py` - `have == need` (all required chars found)
  - `characterReplacement.py` - `(window_size - max_freq) <= k` (can make all same)
  - `lengthOfLongestSubstring.py` - check for duplicates

```python
if valid_condition_met:
    # Process or update result
    result = update_result(window)
```

### 6. **Optimized Maximum Tracking with Deque**
- **Description**: Use a double-ended queue to efficiently track the maximum in a sliding window
- **Key Insight**: Store indices (not values) and remove indices that are out of bounds or can't be max
- **Benefits**: 
  - Reduces max() lookup from O(k) to O(1)
  - Overall time complexity: O(n) instead of O(n*k)
- **Example**: `maxSlidingWindow.py` (deque solution)

```python
from collections import deque
q = deque()  # stores indices

# Remove elements smaller than current (won't be max)
while q and nums[q[-1]] < nums[r]:
    q.pop()

q.append(r)

# Remove elements outside window
if l > q[0]:
    q.popleft()

# Maximum is always at front
if window_complete:
    result.append(nums[q[0]])
```

### 7. **Fixed Window Size**
- **Description**: Slide a window of fixed size k across the array
- **Setup**: Initialize window with first k elements, then expand/shift one element at a time
- **Example**: `maxSlidingWindow.py` - window size fixed at k
- **Key Pattern**: Process result only when window reaches size k

```python
# Initialize first window
for i in range(k):
    # Add element to window

# Slide the window
for i in range(start, end):
    # Add nums[i]
    # Remove nums[i - k]
    # Process current window
```

### 8. **Variable Window Size**
- **Description**: Window size changes based on problem constraints
- **When to use**: Finding minimum/maximum window, managing constraints
- **Examples**:
  - `lengthOfLongestSubstring.py` - window shrinks for duplicates
  - `minWindow.py` - find minimum window size
  - `characterReplacement.py` - window adjusts for replacement limit
  - `checkInclusion.py` - window varies to find permutation

### 9. **Multiple Passes (Edge Case)**
- **Description**: Sometimes need to optimize by iterating through unique elements
- **Use Case**: When brute force sliding window needs optimization
- **Example**: `characterReplacement.py` (alternate solution)
  - Iterate through each unique character
  - Run sliding window for windows containing only that character
  - This guarantees a valid answer even without tracking max frequency globally

```python
for char in unique_chars:
    # Reset window
    left = 0
    count = 0
    for right in range(len(s)):
        # Count only current char
        if s[right] == char:
            count += 1
        # Adjust window
        while (right - left + 1) - count > k:
            left += 1
```

## Time & Space Complexity Summary

| Problem | Time | Space | Key Technique |
|---------|------|-------|----------------|
| Max Sliding Window | O(n*k) or O(n) | O(k) | Two pointers or Deque |
| Longest Substring | O(n) | O(min(m,n)) | Two pointers + Set/Map |
| Min Window | O(n+m) | O(m) | Two pointers + Char count |
| Character Replacement | O(n) or O(n*m) | O(1) or O(m) | Two pointers + Max tracking |
| Check Inclusion | O(n*m) or O(n) | O(m) | Char frequency arrays |
| Max Profit | O(n²) or O(n) | O(1) | Two pointers or DP |

## Common Mistakes to Avoid

1. **Forgetting to shrink window** - Window keeps growing, violating constraints
2. **Wrong condition check** - Condition for validity not properly validated
3. **Not updating result before shrinking** - Miss the valid window before it becomes invalid
4. **Moving left pointer too much** - May skip valid windows
5. **Not handling edge cases** - Empty strings, single elements, impossible windows

## Template

```python
def slidingWindow(s: str, pattern: str) -> type:
    # 1. Initialize two pointers and data structure for tracking
    left = 0
    window_data = {}  # or set, or array
    result = 0  # or []
    
    # 2. Iterate with right pointer to expand window
    for right in range(len(s)):
        # Add element to window
        window_data[s[right]] = window_data.get(s[right], 0) + 1
        
        # 3. Shrink window while condition is violated
        while condition_violated(window_data):
            # Remove element from window
            window_data[s[left]] -= 1
            left += 1
        
        # 4. Update result with valid window
        result = update(result, window_data, left, right)
    
    return result
```
