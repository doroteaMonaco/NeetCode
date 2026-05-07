

from typing_extensions import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]: #if the current height is smaller than the height of the top of the stack, we pop the stack until we find a height that is smaller than the current height. This way, we can find the leftmost index where the current height can extend to.
                stack.pop()
            if stack:
                leftMost[i] = stack[-1] #if the stack is not empty, we set the leftmost index for the current height to be the index of the top of the stack. This is because the current height can extend to the left until it reaches a height that is smaller than it, which is the height at the index of the top of the stack.
            stack.append(i)
        
        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]: #if the current height is smaller than the height of the top of the stack, we pop the stack until we find a height that is smaller than the current height. This way, we can find the rightmost index where the current height can extend to.
                stack.pop()
            if stack:
                rightMost[i] = stack[-1] #if the stack is not empty, we set the rightmost index for the current height to be the index of the top of the stack. This is because the current height can extend to the right until it reaches a height that is smaller than it, which is the height at the index of the top of the stack.
            stack.append(i)

        maxArea = 0
        for i in range(n):
            leftMost[i] += 1 #we add 1 to the leftmost index because we want to include the current height in the area calculation. The leftmost index is the index of the first height that is smaller than the current height, so we need to add 1 to include the current height.
            rightMost[i] -= 1 #we subtract 1 from the rightmost index because we want to include the current height in the area calculation. The rightmost index is the index of the first height that is smaller than the current height, so we need to subtract 1 to include the current height.
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
        return maxArea
    
# Time complexity: O(n) because we traverse the heights array three times (once for finding the leftmost indices, once for finding the rightmost indices, and once for calculating the area).
# Space complexity: O(n) because we use two additional arrays (leftMost and rightMost) to store the leftmost and rightmost indices for each height.

#Others solutions
#Segment Tree: We can build a segment tree to store the minimum height in a given range. Then, we can use a divide-and-conquer approach to find the largest rectangle area by recursively finding the minimum height in the current range and calculating the area based on that height.

class MinIdx_Segtree:
    def __init__(self, N, A):
        self.n = N
        self.INF = int(1e9)
        self.A = A
        while (self.n & (self.n - 1)) != 0: #if n is not a power of 2, we need to pad the array with INF values until it becomes a power of 2. This is because a segment tree requires the number of elements to be a power of 2 for efficient indexing.
            self.A.append(self.INF)
            self.n += 1
        self.tree = [0] * (2 * self.n) #we create a segment tree array of size 2*n to store the indices of the minimum heights in the given range. The first n elements of the tree will store the indices of the minimum heights for the leaf nodes, and the remaining n elements will store the indices of the minimum heights for the internal nodes.
        self.build()

    def build(self):
        for i in range(self.n):
            self.tree[self.n + i] = i
        for j in range(self.n - 1, 0, -1):
            a = self.tree[j << 1] #the left child of the current node is at index j << 1 (which is equivalent to j * 2), and the right child is at index (j << 1) + 1 (which is equivalent to j * 2 + 1). We compare the heights at these two indices and store the index of the smaller height in the current node.
            b = self.tree[(j << 1) + 1] #the right child of the current node is at index (j << 1) + 1 (which is equivalent to j * 2 + 1). We compare the heights at these two indices and store the index of the smaller height in the current node.
            if self.A[a] <= self.A[b]:
                self.tree[j] = a
            else:
                self.tree[j] = b

    def update(self, i, val):
        self.A[i] = val
        j = (self.n + i) >> 1
        while j >= 1:
            a = self.tree[j << 1] #the left child of the current node is at index j << 1 (which is equivalent to j * 2), and the right child is at index (j << 1) + 1 (which is equivalent to j * 2 + 1). We compare the heights at these two indices and store the index of the smaller height in the current node.
            b = self.tree[(j << 1) + 1] #the right child of the current node is at index (j << 1) + 1 (which is equivalent to j * 2 + 1). We compare the heights at these two indices and store the index of the smaller height in the current node.
            if self.A[a] <= self.A[b]:
                self.tree[j] = a
            else:
                self.tree[j] = b
            j >>= 1

    def query(self, ql, qh):
        return self._query(1, 0, self.n - 1, ql, qh) #we start the query from the root of the segment tree (which is at index 1) and the range of the entire array (which is from 0 to n - 1). We will recursively traverse the segment tree to find the index of the minimum height in the given query range (ql to qh).

    def _query(self, node, l, h, ql, qh):
        if ql > h or qh < l:
            return self.INF
        if l >= ql and h <= qh: #if the current node's range (l to h) is completely within the query range (ql to qh), we can return the index of the minimum height stored in the current node. This is because the segment tree is built in such a way that each node stores the index of the minimum height for its corresponding range.
            return self.tree[node]
        a = self._query(node << 1, l, (l + h) >> 1, ql, qh) #we recursively query the left child of the current node (which is at index node << 1) for the range from l to (l + h) >> 1 (which is the midpoint of the current node's range). This will give us the index of the minimum height in the left half of the current node's range.
        b = self._query((node << 1) + 1, ((l + h) >> 1) + 1, h, ql, qh) #we recursively query the right child of the current node (which is at index (node << 1) + 1) for the range from ((l + h) >> 1) + 1 to h (which is the right half of the current node's range). This will give us the index of the minimum height in the right half of the current node's range.
        if a == self.INF: #if the left child query returns INF, it means that there are no valid indices in the left half of the current node's range, so we can return the index from the right child query.
            return b
        if b == self.INF: #if the right child query returns INF, it means that there are no valid indices in the right half of the current node's range, so we can return the index from the left child query.
            return a
        return a if self.A[a] <= self.A[b] else b

class Solution:
    def getMaxArea(self, heights, l, r, st):
        if l > r: #if the left index is greater than the right index, it means that there are no valid indices in the current range, so we can return 0 as the area for this range.
            return 0
        if l == r: #if the left index is equal to the right index, it means that there is only one bar in the current range, so we can return its height as the area for this range.
            return heights[l]
        minIdx = st.query(l, r) #we query the segment tree to find the index of the minimum height in the current range (from l to r). This will give us the index of the height that limits the area for the current range.
        return max(max(self.getMaxArea(heights, l, minIdx - 1, st), #we recursively calculate the maximum area for the left half of the current range (from l to minIdx - 1) and the right half of the current range (from minIdx + 1 to r). We take the maximum of these two areas and compare it with the area calculated using the minimum height (which is heights[minIdx] * (r - l + 1)) to find the maximum area for the current range. This is because the area for the current range can be limited by the minimum height, but it can also be limited by the areas in the left and right halves of the current range, so we need to consider all three possibilities to find the maximum area.
                       self.getMaxArea(heights, minIdx + 1, r, st)),
                   (r - l + 1) * heights[minIdx])

    def largestRectangleArea(self, heights):
        n = len(heights)
        st = MinIdx_Segtree(n, heights)
        return self.getMaxArea(heights, 0, n - 1, st)