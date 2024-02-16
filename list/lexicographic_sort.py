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


# Time complexity: O(n)
# Space complexity: O(1), not counting space for result list
class LexicalSort:
    def sort(self, n: int) -> list[int]:
        res = [num for num in range(1, n+1)]
        return sorted(res, key=str)


if __name__ == "__main__":
    ls = LexicalSort()
    print(ls.sort(19))


# Another algo using heaps
# (Time complexity: O(n), Space: O(n))
# heap = [(str(i), i) for i in range(1, n + 1)]
# heapify(heap)
# res = []
# while heap:
#     _, num = heappop(heap)
#     res.append(num)
#
# return res
