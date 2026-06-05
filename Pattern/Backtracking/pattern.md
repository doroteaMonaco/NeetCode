# Backtracking Patterns

## 1. Combination Sum Pattern
**File:** `combinationSum.py`

**Caratteristiche:**
- Trovare combinazioni che sommano a un target
- Elementi possono essere riutilizzati
- Start index per evitare duplicati diversi
- Pruning: target < 0 o raggiunto

**Implementazione chiave:**
```python
def dfs(i, cur, total):
    if total == target:
        res.append(cur.copy())
        return
    for j in range(i, len(nums)):
        if total + nums[j] > target:
            return
        cur.append(nums[j])
        dfs(j, cur, total + nums[j])  # i non incrementa, permette ripetizioni
        cur.pop()
```

**Complessità:**
- Time: O(2^t) dove t è il target
- Space: O(t) ricorsione + output

---

## 2. Combination Sum II Pattern
**File:** `combinationSumII.py`

**Caratteristiche:**
- Combinazioni senza ripetizione di elementi
- Sort prima del backtracking
- Skip duplicati: `if i > start and candidates[i] == candidates[i-1]`
- Early termination: `if candidates[i] > target: break`

**Implementazione chiave:**
```python
def combinations_without_repetitions(start, sol, candidates, target):
    if target == 0:
        res.append(list(sol))
        return
    for i in range(start, len(candidates)):
        if i > start and candidates[i] == candidates[i - 1]:
            continue
        if candidates[i] > target:
            break
        sol.append(candidates[i])
        combinations_without_repetitions(i + 1, sol, candidates, target - candidates[i])
        sol.pop()
```

**Complessità:**
- Time: O(n * 2^n)
- Space: O(n)

---

## 3. Generate Parenthesis Pattern
**File:** `generateParenthesis.py`

**Caratteristiche:**
- Validazione durante backtracking
- Tracking di open/closed parentheses
- Constraint: `closedP < openP` (valide solo se abbiamo aperto prima)
- Costruzione di stringhe

**Implementazione chiave:**
```python
def backtracking(sol, n, openP, closedP, l):
    if len(sol) == l:
        string = "".join(sol)
        res.append(string)
        return
    if openP < n:
        sol.append("(")
        backtracking(sol, n, openP + 1, closedP, l)
        sol.pop()
    if closedP < openP:
        sol.append(")")
        backtracking(sol, n, openP, closedP + 1, l)
        sol.pop()
```

**Complessità:**
- Time: O(4^n / √n) - Catalan number
- Space: O(n)

---

## 4. Letter Combinations Pattern
**File:** `letterCombinations.py`

**Caratteristiche:**
- Mapping da digit a lettere
- Iterare su lettere mappate
- Costruzione progressiva di stringhe
- Early return per input vuoto

**Implementazione chiave:**
```python
def backtracking(index, sol):
    if len(sol) == len(digits):
        res.append(sol)
        return
    letters = num_letters[digits[index]]
    for l in letters:
        backtracking(index + 1, sol + l)
```

**Complessità:**
- Time: O(4^n * n) dove n è lunghezza digits
- Space: O(n)

---

## 5. N Queens Pattern
**File:** `NQueens.py`

**Caratteristiche:**
- Constraint checking con sets (colonne, diagonali, anti-diagonali)
- Placement su matrice 2D
- Markatura di constraints durante backtracking
- Unmarkatura durante backtracking
- Diagonale: `r - c`, Anti-diagonale: `r + c`

**Implementazione chiave:**
```python
def backtracking(m, n, r):
    if r == n:
        res.append(sol)
        return
    for c in range(n):
        if c in cols or (r + c) in anti_diags or (r - c) in diags:
            continue
        cols.add(c)
        diags.add(r - c)
        anti_diags.add(r + c)
        m[r][c] = "Q"
        
        backtracking(m, n, r + 1)
        
        cols.remove(c)
        diags.remove(r - c)
        anti_diags.remove(r + c)
        m[r][c] = "."
```

**Complessità:**
- Time: O(n!)
- Space: O(n)

---

## 6. Palindrome Partition Pattern
**File:** `PalindromePartition.py`

**Caratteristiche:**
- Validazione tramite funzione helper (isPalindrome)
- Partizione ricorsiva di stringhe
- Aggiunta solo se partition è valida
- Base case: `start == len(s)`

**Implementazione chiave:**
```python
def backtracking(s, start, sol):
    if start == len(s):
        res.append(list(sol))
        return
    for end in range(start + 1, len(s) + 1):
        sub = s[start:end]
        if isPalindrome(sub):
            sol.append(sub)
            backtracking(s, end, sol)
            sol.pop()
```

**Complessità:**
- Time: O(n * 2^n) - 2^n partizioni, O(n) per validare palindrome
- Space: O(n)

---

## 7. Permutations Pattern
**File:** `Permutations.py`

**Caratteristiche:**
- Array booleano per tracciare elementi usati
- Tutti gli elementi devono essere inclusi
- Nessun elemento può essere usato due volte
- Base case: `len(sol) == n`

**Implementazione chiave:**
```python
def permutations(sol, nums, mark, n):
    if len(sol) == n:
        res.append(list(sol))
        return
    for i in range(n):
        if not mark[i]:
            mark[i] = True
            sol.append(nums[i])
            permutations(sol, nums, mark, n)
            sol.pop()
            mark[i] = False
```

**Complessità:**
- Time: O(n * n!)
- Space: O(n)

---

## 8. Subsets Pattern
**File:** `Subsets.py`

**Caratteristiche:**
- Bitmask approach: per ogni elemento 0 (escludi) o 1 (includi)
- Tutti i 2^n subset generati
- Nessuna validazione di constraint
- Ricorsione su posizioni

**Implementazione chiave:**
```python
def powerset_bitmask(nums, pos, sol, n):
    if pos == n:
        powerset = [nums[i] for i in range(n) if sol[i] == 1]
        res.append(powerset)
        return
    sol[pos] = 0
    powerset_bitmask(nums, pos + 1, sol, n)
    sol[pos] = 1
    powerset_bitmask(nums, pos + 1, sol, n)
```

**Complessità:**
- Time: O(n * 2^n)
- Space: O(n)

---

## 9. Subsets with Duplicates Pattern
**File:** `subsetsWithDup.py`

**Caratteristiche:**
- Sort array per raggruppare duplicati
- Skip duplicati: `if i > start and nums[i] == nums[i-1]: continue`
- Append solution all'inizio della ricorsione
- Non ripete elementi identici in subset differenti

**Implementazione chiave:**
```python
def powerset(sol, nums, start, n):
    res.append(list(sol))
    for i in range(start, n):
        if i > start and nums[i] == nums[i - 1]:
            continue
        sol.append(nums[i])
        powerset(sol, nums, i + 1, n)
        sol.pop()
```

**Complessità:**
- Time: O(n * 2^n)
- Space: O(n)

---

## Pattern Summary

| Pattern | Caratteristica | Constraint | Ripetizione |
|---------|---|---|---|
| Combination Sum | Target sum | target >= 0 | ✓ Permessa |
| Combination Sum II | Target sum | Elementi unici | ✗ Vietata |
| Generate Parenthesis | Validazione | openP/closedP | ✗ Vietata |
| Letter Combinations | Mapping | Tutte le lettere | N/A |
| N Queens | Placement | cols, diag, anti-diag | N/A |
| Palindrome Partition | Validazione | isPalindrome | N/A |
| Permutations | Ordine | Tutti elementi | ✗ Vietata |
| Subsets | Inclusione/esclusione | Nessuno | ✗ Vietata |
| Subsets with Dup | Inclusione/esclusione + Skip | Skip duplicati | ✗ Vietata |

---

## Template Generale Backtracking

```python
def backtrack(start, current, constraint_state):
    # Base case: soluzione trovata
    if is_solution(current):
        result.append(copy(current))
        return
    
    # Explore candidates
    for candidate in get_candidates(start):
        # Constraint check
        if is_valid(candidate, constraint_state):
            # Include
            current.append(candidate)
            update_state(constraint_state)
            
            # Recurse
            backtrack(next_start, current, constraint_state)
            
            # Backtrack
            current.pop()
            revert_state(constraint_state)
```
