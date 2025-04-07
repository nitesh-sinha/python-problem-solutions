# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# Example 3:

# Input: nums = [1,0,1,2]
# Output: 3
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                # new streak begins here
                next_num = num + 1
                while next_num in nums:
                    next_num = next_num + 1
                max_len = max(max_len, next_num - num)
            
        return max_len
    


    # Algorithm 2(Time complexity: O(nlogn), Space complexity: O(1)) :
    # if len(nums) <= 1:
    #     return len(nums)

    # max_len = 0
    # longest_consec_len = 1
    # nums.sort()
    # for idx in range(len(nums)):
    #     if idx + 1 < len(nums):
    #         consec_diff = nums[idx+1] - nums[idx]
    #         if consec_diff <= 1:
    #             longest_consec_len += consec_diff
    #         else:
    #             max_len = max(longest_consec_len, max_len)
    #             longest_consec_len = 1

    # max_len = max(longest_consec_len, max_len)
    # return max_len