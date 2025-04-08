# Create a problem statement for this algorithm
# Given an array of integers, sort the array in ascending order using the counting sort algorithm.

# Time Complexity: O(n + k), where n = no. of elements in the array, k= range of the elements
# Space Complexity: O(n + k)


class Sort:
	# This algo can handle both positive and negative numbers
	def countingSort(self, nums: list[int]) -> list[int]:
		if len(nums) <= 1:
			return nums

		result = []
		min_num, max_num = min(nums), max(nums)
		count = [0] * (max_num - min_num + 1)

		for num in nums:
			count[num - min_num] += 1        # Shift index to handle negatives

		for idx in range(len(count)):
			while count[idx] > 0:
				result.append(idx + min_num) # Shift back to original value
				count[idx] -= 1

		return result