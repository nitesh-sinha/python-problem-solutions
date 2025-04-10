# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


class MaxSubarraySum:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Intuition: Use a variable to keep track of the current subarray sum
    # and update the max sum if the current subarray sum is greater than the max sum
    # If the current subarray sum is less than the current element, reset the current subarray sum to the current element
    # This is because we are looking for the subarray with the largest sum
    # Kadane's algorithm: https://en.wikipedia.org/wiki/Kadane%27s_algorithm
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        cur_subarray_sum = nums[0]
        for idx in range(1, len(nums)):
            cur_subarray_sum = cur_subarray_sum + nums[idx] if \
                cur_subarray_sum + nums[idx] > nums[idx] else nums[idx]
            max_sum = max(cur_subarray_sum, max_sum)

        return max_sum
