# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

# Time Complexity: O(n)
# Space Complexity: O(n)

class NumWaysToClimb:
    # Intuition: To climb nth stair, you can either 
    # come from (n-1)th stair or (n-2)th stair
    # So, the number of ways to climb nth stair is the 
    # sum of the number of ways to climb (n-1)th stair and (n-2)th stair
    def climbStairs(self, n: int) -> int:
        num_ways_to_top = [1] * (n+1)
        for idx in range(2, len(num_ways_to_top)):
            num_ways_to_top[idx] = num_ways_to_top[idx-1] + num_ways_to_top[idx-2]
        
        return num_ways_to_top[n]