# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to wait after
# the ith day to get a warmer temperature. If there is no future day for which this is possible,
# keep answer[i] == 0 instead.
#
# Example 1:
#
# Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
#
# Example 2:
#
# Input: temperatures = [30, 40, 50, 60]
# Output: [1, 1, 1, 0]
#
# Example 3:
#
# Input: temperatures = [30, 60, 90]
# Output: [1, 1, 0]
#
# Constraints:
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

# Time complexity: O(N) where N=no. of elements in input list as it uses a monotonically decreasing stack.
#                     Every element in the input is pushed and popped from stack at most once.
#                     Hence the inner while loop is executed total of N times across all iterations of outer for loop.
#                     Hence while loop's complexity is constant O(1)

# Space complexity: O(N) for the next_larger_temp stack

class DailyTemp:
    def get_wait_next_hot_day(self, temperatures: list[int]) -> list[int]: 
        next_larger_temp = [(temperatures[-1], len(temperatures) - 1)]
        prev_temp = temperatures[-1]
        wait_days = [0 for i in range(len(temperatures))]
        for idx in range(len(temperatures) - 2, -1, -1):
            cur_temp = temperatures[idx]
            if cur_temp < prev_temp:
                wait_days[idx] = 1
            else:
                (tos_temp, tos_idx) = next_larger_temp[-1]
                while cur_temp >= tos_temp:
                    next_larger_temp.pop()
                    if len(next_larger_temp) > 0:
                        tos_temp, tos_idx = next_larger_temp[-1]
                    else:
                        break

                # either cur_temp < TOS OR stack is empty
                # in either case add cur_temp to TOS
                if len(next_larger_temp) > 0:
                    # TOS is not empty i.e. found a larger temp
                    wait_days[idx] = tos_idx - idx
                else:
                    wait_days[idx] = 0

            # add cur_temp to TOS
            next_larger_temp.append((cur_temp, idx))
            prev_temp = cur_temp
        return wait_days
