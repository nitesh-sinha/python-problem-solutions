# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.
#
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
# Constraints:
# 0 <= n <= 105


class BitCounter:
    # Solution is a mix of DP and bitwise operations
    # Algo: Count of 1's in any number N = )Count of
    # 1 in last bit of N) + (Count of 1's in N/2)
    # since N/2 is simply a right shifted version of N by 1 bit
    def count(self, n: int) -> list[int]:
        ans = [0] * (n+1) # ans[i] stores count of 1's in i
        for num in range(1, n+1):
            current_bit = num & 1
            ans[num] = ans[num//2] + current_bit
        return ans


if __name__ == "__main__":
    counter = BitCounter()
    print(counter.count(5))
    print(counter.count(10))
