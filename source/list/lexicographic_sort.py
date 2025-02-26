# Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
#
# Example 1:
# Input: n = 13
# Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
#
# Example 2:
# Input: n = 2
# Output: [1,2]
#
# Constraints:
# 1 <= n <= 5 * 10^4


# Time complexity: O(n * log(n))
# Space complexity: O(n), not counting space for result list
class LexicalSort:
    def sort(self, n: int) -> list[int]:
        nums = [num for num in range(1,n+1)]
        nums_len = len(nums)
        if nums_len <= 1:
            return nums
        self.merge_sort(nums, 0, nums_len-1)
        return nums

    def merge_sort(self, nums, low, high):
        if low>=high:
            return
        mid = low + (high-low)//2
        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid+1, high)
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        out_buff = [0 for _ in nums]
        buff_idx = low
        l_ptr, r_ptr = low, mid+1
        while l_ptr <= mid and r_ptr<=high:
            if str(nums[l_ptr]) <= str(nums[r_ptr]):
                out_buff[buff_idx] = nums[l_ptr]
                l_ptr += 1
            else:
                out_buff[buff_idx] = nums[r_ptr]
                r_ptr += 1
            buff_idx += 1

        while l_ptr <= mid:
            out_buff[buff_idx] = nums[l_ptr]
            l_ptr += 1
            buff_idx += 1

        while r_ptr <= high:
            out_buff[buff_idx] = nums[r_ptr]
            r_ptr += 1
            buff_idx += 1

        nums[low:high+1] = out_buff[low:high+1]


if __name__ == "__main__":
    ls = LexicalSort()
    print(ls.sort(120))


# Algo 2: using heaps
# (Time complexity: O(n), Space: O(n))
# heap = [(str(i), i) for i in range(1, n + 1)]
# heapify(heap)
# res = []
# while heap:
#     _, num = heappop(heap)
#     res.append(num)
#
# return res


# Algo 3: using inbuilt sorted method
# res = [num for num in range(1, n+1)]
# return sorted(res, key=str)


