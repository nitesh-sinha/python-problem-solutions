# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

# Time Complexity: O(m+n)

import math


class SortedListsMedian:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        median = math.ceil((len1 + len2) / 2)
        while median > 1 and idx1 < len1 and idx2 < len2:
            if nums1[idx1] <= nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
            median -= 1

        # It is possible that one of the list
        # got exhausted during iteration
        # but we haven't yet reached the middle element
        while median > 1:
            if idx1 < len1:
                idx1 += 1
            else:
                idx2 += 1
            median -= 1

        if (len1 + len2) % 2 != 0:
            # odd number of total elements
            if idx1 < len1 and idx2 < len2:
                return float(min(nums1[idx1], nums2[idx2]))
            elif idx1 < len1:
                # nums2 is exhausted
                return float(nums1[idx1])
            else:
                # nums1 is exhausted
                return float(nums2[idx2])
        else:
            # even total elements
            if idx1 < len1 and idx2 < len2:
                # find median using least 2 nums
                # among nums1[idx1], nums1[idx1+1],
                # nums2[idx2] and nums2[idx2+1]
                temp = [nums1[idx1], nums2[idx2]]
                if idx1 + 1 < len1:
                    temp.append(nums1[idx1 + 1])
                if idx2 + 1 < len2:
                    temp.append(nums2[idx2 + 1])
                temp.sort()
                return (temp[0] + temp[1]) / 2
            elif idx1 < len1:
                # nums2 is exhausted
                return (nums1[idx1] + nums1[idx1 + 1]) / 2
            else:
                # nums1 is exhausted
                return (nums2[idx2] + nums2[idx2 + 1]) / 2
