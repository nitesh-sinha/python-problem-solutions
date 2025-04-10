# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

# Time Complexity: O(n * m) where n is the number of coins and m is the amount
# Space Complexity: O(m)

class MinCoinChangeCalculator:
    def coinChange(self, coins: list[int], amount: int) -> int:
        min_coins_for_amount = [0] * (amount + 1)

        for idx in range(1, len(min_coins_for_amount)):
            min_coins = float('inf')
            for coin in coins:
                if idx - coin >= 0:
                    min_coins = min(min_coins, min_coins_for_amount[idx-coin])
            
            min_coins_for_amount[idx] = 1 + min_coins if min_coins != float('inf') else min_coins

        res = min_coins_for_amount[amount] if min_coins_for_amount[amount] != float('inf') else -1
        return res