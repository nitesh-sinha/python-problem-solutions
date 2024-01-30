# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
#
#
# Example 1:
# Input: nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
#
# Example 2:
# Input: nums = [0, 1]
# Output: [[0, 1], [1, 0]]
#
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.


class Permute:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        temp = []
        self.get_permutations(nums, temp, res)
        return res

    def get_permutations(self, nums, temp, res):
        if len(temp) == len(nums):
            res.append(
                temp.copy())  # save a copy of temp to avoid changes to the saved list in subsequent processing of temp
            return

        for num in nums:
            if num in temp:
                continue
            temp.append(num)
            self.get_permutations(nums, temp, res)
            temp.pop()


if __name__ == "__main__":
    p = Permute()
    print(p.permute([1,2,3]))
    print(p.permute([1,2]))
    print(p.permute([1]))