# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.
#
# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or
# return -1 if n has less than k factors.
#
# Example 1:
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
#
# Example 2:
# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
#
# Example 3:
# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
#
# Constraints:
# 1 <= k <= n <= 1000

# Time complexity: O(sqrt(n))
# Space complexity: O(1)

import math


class KthFactor:
    def get_factor(self, n: int, k: int) -> int:
        sqrt_n = math.sqrt(n)
        # Don't count sqrt_n twice
        # Go upto ceil(sqrt_n) - not including it
        for i in range(1, math.ceil(sqrt_n)):
            if n % i == 0:
                if k == 1:
                    return i
                else:
                    k = k - 1

        # Start from floor(sqrt_n) - including it
        for i in range(math.floor(sqrt_n), 0, -1):
            if n % i == 0:
                if k == 1:
                    return int(n / i)
                else:
                    k = k - 1
        # k factors of n don't exist
        return -1

