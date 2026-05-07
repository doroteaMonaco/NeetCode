# Stack Patterns

## Main patterns

1. Monotonic stack
   - Maintain a stack where elements stay in a strictly increasing or decreasing order.
   - Used in `dailyTemperatures.py`, `largestRectangleArea.py`, and `carFleet.py`.
   - Examples:
     - keep a decreasing stack of (index, temperature) pairs to find the next warmer day in `dailyTemperatures`
     - run two monotonic stacks (left-to-right and right-to-left) to find the nearest smaller bar on each side for `largestRectangleArea`
     - after sorting cars by position descending, use a stack of arrival times to detect when a faster car catches the fleet ahead in `carFleet`

2. Bracket / delimiter matching
   - Push opening delimiters onto the stack; on each closing delimiter pop and verify the match.
   - Used in `validParenthesis.py` with a hash map that maps each closing bracket to its expected opening bracket.

3. Stack-based expression evaluation
   - Push operands; on each operator pop two operands, apply the operation, and push the result back.
   - Used in `evalRPN.py` to evaluate Reverse Polish Notation in a single left-to-right pass.

4. Auxiliary / parallel stack for metadata
   - Maintain a secondary stack in sync with the main stack to track extra per-level information (e.g., running minimum).
   - Used in `minStack.py` where `minStack` stores the current minimum after every push, enabling O(1) `getMin`.

5. Sort then stack
   - Sort input by a key that defines processing order, then apply stack logic.
   - Used in `carFleet.py`: sort (position, speed) pairs by position descending so cars closer to the target are processed first, then use a stack to merge fleets.

## Supporting complexity insights

- Monotonic stack solutions typically run in O(n) time because each element is pushed and popped at most once.
- `largestRectangleArea` uses two O(n) passes (left boundaries, right boundaries) plus a final O(n) scan, giving O(n) overall with O(n) extra space.
- `evalRPN` is O(n) time and O(n) space (stack grows proportionally to the number of operands).
- `validParenthesis` is O(n) time and O(n) space in the worst case (all opening brackets).
- `minStack` achieves O(1) for all operations at the cost of O(n) extra space for the parallel min-stack.
- `carFleet` is O(n log n) due to sorting; the stack pass itself is O(n).
