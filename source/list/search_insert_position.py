# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4
#
# Constraints:
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4

# Time complexity: O(log n) where n=no. of elements in nums

class Search:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid

        # lo == hi here
        if target <= nums[lo]:
            return lo

        return 1 + lo
