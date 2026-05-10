# Binary Search Patterns

---

## 1. Classic Binary Search (`binarySearch.py`)

**Use when:** array is sorted, looking for an exact target.

```python
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if nums[m] == target:
        return m
    elif nums[m] < target:
        l = m + 1
    else:
        r = m - 1
return -1
```

**Variants:**
- **Recursive:** same logic, O(log n) stack space.
- **Lower bound** (`l < r`, `r = m` or `l = m + 1`): finds leftmost valid position. Loop ends when `l == r` pointing at the answer.

**Complexity:** Time O(log n) | Space O(1) iterative, O(log n) recursive.

---

## 2. Binary Search on Answer Space (`kokoEatingBananas.py`)

**Use when:** you need to find the minimum/maximum *value* satisfying a condition (not a position in an array).

```
left, right = min_possible, max_possible
result = right

while left <= right:
    m = (left + right) // 2
    if condition_holds(m):        # e.g. hoursRequired <= h
        result = m
        right = m - 1             # try to minimize
    else:
        left = m + 1

return result
```

**Key insight:** define a helper that checks whether a candidate value is feasible, then binary search over the candidate range.

**Complexity:** Time O(n · log(max_val)) | Space O(1).

---

## 3. Binary Search on a 2D Matrix (`searchMatrix.py`)

**Use when:** a sorted m×n matrix can be treated as a flat sorted array.

```python
i, j = 0, ROWS * COLS - 1
while i <= j:
    m = (i + j) // 2
    r, c = m // COLS, m % COLS    # map flat index → (row, col)
    if matrix[r][c] == target: return True
    elif matrix[r][c] < target: i = m + 1
    else: j = m - 1
return False
```

**Variant – Staircase search** (matrix rows & columns sorted independently):  
Start at top-right corner; move left if too large, down if too small. O(m + n).

**Complexity (BS):** Time O(log(m·n)) | Space O(1).

---

## 4. Find Minimum in Rotated Sorted Array (`minSearch.py`)

**Use when:** array was sorted then rotated; need to find the rotation pivot / minimum element.

```python
l, r = 0, len(nums) - 1
while l < r:
    m = (l + r) // 2
    if nums[m] < nums[r]:   # minimum is in the left half (inclusive of m)
        r = m
    else:                   # minimum is in the right half
        l = m + 1
return nums[l]
```

**Key insight:** compare `nums[m]` with `nums[r]` (not with `nums[l]`) to decide which side the rotation inflection is on.

**Complexity:** Time O(log n) | Space O(1).

---

## 5. Search in Rotated Sorted Array (`searchRotateVector.py`)

**Use when:** array is rotated and you need to find a target.

**Two-pass approach:**
1. Find pivot (minimum index) using the pattern above.
2. Determine which sorted half contains the target, then run classic binary search on that half.

**One-pass approach:** at each step determine which half is *sorted*, then check if the target lies in that half:

```python
while l <= r:
    m = (l + r) // 2
    if nums[m] == target: return m
    if nums[l] <= nums[m]:           # left half is sorted
        if nums[l] <= target < nums[m]: r = m - 1
        else: l = m + 1
    else:                            # right half is sorted
        if nums[m] < target <= nums[r]: l = m + 1
        else: r = m - 1
return -1
```

**Complexity:** Time O(log n) | Space O(1).

---

## 6. Binary Search for Predecessor / Upper Bound (`timeMap.py`)

**Use when:** timestamps (or values) are sorted and you need the largest entry ≤ a given query.

```python
left, right = 0, len(timestamps) - 1
best = -1
while left <= right:
    m = (left + right) // 2
    if timestamps[m] <= query:
        best = m          # record last valid position
        left = m + 1      # try to go further right
    else:
        right = m - 1
return values[best] if best != -1 else ""
```

**Key insight:** keep a `best` (or `index`) variable updated every time the condition holds; at the end it holds the rightmost valid index.

**Alternative:** `SortedDict` + `bisect_right(timestamp) - 1` for O(log n) per operation with cleaner code.

**Complexity:** Time O(log n) per query | Space O(n) total storage.

---

## 7. Binary Search on Partition (Median of Two Sorted Arrays) (`findMedianSortedArrays.py`)

**Use when:** you must find the k-th element across two sorted arrays in O(log(m+n)).

**Core idea:** binary search on the partition index `i` of the smaller array A. The partition index `j` of B is derived as `half - i - 2`. A valid partition satisfies:

```
A[i] <= B[j+1]  and  B[j] <= A[i+1]
```

```python
l, r = 0, len(A) - 1
while True:
    i = (l + r) // 2
    j = half - i - 2
    Aleft  = A[i]   if i >= 0        else -inf
    Aright = A[i+1] if i+1 < len(A) else +inf
    Bleft  = B[j]   if j >= 0        else -inf
    Bright = B[j+1] if j+1 < len(B) else +inf

    if Aleft <= Bright and Bleft <= Aright:
        if total % 2: return min(Aright, Bright)
        return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
    elif Aleft > Bright:
        r = i - 1
    else:
        l = i + 1
```

Always binary-search on the **smaller** array to keep complexity minimal.

**Complexity:** Time O(log(min(m, n))) | Space O(1).

---

## Quick Reference

| Pattern | Condition to move right | Loop invariant |
|---|---|---|
| Classic BS | `nums[m] < target` → `l = m+1` | `l <= r` |
| Lower bound | `nums[m] >= target` → `r = m` | `l < r` |
| Answer space | condition fails → `l = m+1` | `l <= r` |
| Min in rotated | `nums[m] >= nums[r]` → `l = m+1` | `l < r` |
| Predecessor | `ts[m] <= query` → save & `l = m+1` | `l <= r` |
| Partition BS | `Aleft > Bright` → `r = i-1` | infinite loop, exits on valid partition |
