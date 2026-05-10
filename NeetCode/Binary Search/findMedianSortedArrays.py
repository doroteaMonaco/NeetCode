
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity") 
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright: # if the left side of A is less than or equal to the right side of B and the left side of B is less than or equal to the right side of A, it means that we have found the correct partition. The median can be calculated based on whether the total number of elements is odd or even. If the total number of elements is odd, the median is the minimum of the right sides of A and B. If the total number of elements is even, the median is the average of the maximum of the left sides of A and B and the minimum of the right sides of A and B.
                if total % 2: # if the total number of elements is odd, the median is the minimum of the right sides of A and B
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 # if the total number of elements is even, the median is the average of the maximum of the left sides of A and B and the minimum of the right sides of A and B
            elif Aleft > Bright: # if the left side of A is greater than the right side of B, it means that we need to move the partition in A to the left. Therefore, we can move the right pointer to i - 1 to search for the correct partition in the left half of A.
                r = i - 1
            else:
                l = i + 1 # if the left side of B is greater than the right side of A, it means that we need to move the partition in A to the right. Therefore, we can move the left pointer to i + 1 to search for the correct partition in the right half of A.
    

# Time complexity: O(log(m + n)) where m and n are the lengths of the two input arrays. This is because we are performing a binary search on the combined length of the two arrays to find the k-th smallest element, which takes O(log(m + n)) time.
# Space complexity: O(1) because we are using only a constant amount of extra space

# Other solution:
# Binary search lower bound
class Solution:
    def get_kth(self, a: List[int], m: int, b: List[int], n: int, k: int, a_start: int = 0, b_start: int = 0) -> int:
        if m > n: # if the length of array a is greater than the length of array b, we can swap the arrays and their lengths to ensure that we are always performing the binary search on the smaller array. This helps to optimize the search process and reduce the time complexity.
            return self.get_kth(b, n, a, m, k, b_start, a_start)
        if m == 0: # if the length of array a is 0, it means that all the elements in array b are greater than the k-th smallest element. Therefore, we can directly return the k-th smallest element from array b, which is located at index b_start + k - 1.
            return b[b_start + k - 1]
        if k == 1: # if k is 1, it means that we are looking for the smallest element among the remaining elements in both arrays. Therefore, we can return the minimum of the first elements of both arrays, which are located at index a_start and b_start respectively.
            return min(a[a_start], b[b_start])

        i = min(m, k // 2)
        j = min(n, k // 2)

        if a[a_start + i - 1] > b[b_start + j - 1]:
            return self.get_kth(a, m, b, n - j, k - j, a_start, b_start + j)
        else:
            return self.get_kth(a, m - i, b, n, k - i, a_start + i, b_start)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = (len(nums1) + len(nums2) + 1) // 2 # if the total number of elements is odd, the median is the k-th smallest element where k is (m + n + 1) // 2. If the total number of elements is even, the median is the average of the k-th and (k + 1)-th smallest elements where k is (m + n) // 2. Therefore, we can calculate left as (len(nums1) + len(nums2) + 1) // 2 to find the k-th smallest element for both odd and even cases.
        right = (len(nums1) + len(nums2) + 2) // 2
        return (self.get_kth(nums1, len(nums1), nums2, len(nums2), left) +
                self.get_kth(nums1, len(nums1), nums2, len(nums2), right)) / 2.0
    
# Time complexity: O(log(m + n)) where m and n are the lengths of the two input arrays. This is because we are performing a binary search on the combined length of the two arrays to find the k-th smallest element, which takes O(log(m + n)) time.
# Space complexity: O(1) because we are using only a constant amount of extra space

#Two pointers solution
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        median1 = median2 = 0

        for count in range((len1 + len2) // 2 + 1): # we need to iterate until we reach the middle index of the combined length of the two arrays. This is because the median is the middle element (or the average of the two middle elements) when the two arrays are combined and sorted. Therefore, we need to iterate until we reach the index (len1 + len2) // 2 to find the median element(s).
            median2 = median1
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1

        if (len1 + len2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2.0
        
# Time complexity: O(m + n) where m and n are the lengths of the two input arrays. This is because we are iterating through both arrays until we reach the middle index of the combined length, which takes O(m + n) time in the worst case.
# Space complexity: O(1) because we are using only a constant amount of extra space