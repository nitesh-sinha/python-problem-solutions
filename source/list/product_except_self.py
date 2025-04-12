# Given an integer array nums, return an array answer such that answer[i] is equal to the 
# product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


#             Time Complexity: O(n)
#             Space Complexity: O(n)
#                               For O(1) space complexity, we can use res array itself 
#                               to store product_from_end results in the beginning,
#                               and then iterate through the nums and res array to 
#                               calculate the final result

class ProductOfArrayExceptSelf:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product_from_end = []
        prod = 1
        for idx in range(len(nums)-1, -1, -1):
            prod *= nums[idx]
            product_from_end.append(prod)
        product_from_end.reverse()
        product_from_end.append(1)

        res = []
        prod = 1
        for idx in range(1, len(product_from_end)):
            res.append(prod*product_from_end[idx])
            prod *= nums[idx-1]
        return res
