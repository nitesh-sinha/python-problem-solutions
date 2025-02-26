# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
#
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
# Constraints:
#
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# Time complexity: O(n * log n) where n = number of intervals

class IntervalsMerger:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals

        merged_intervals = []
        intervals.sort() # sorts in ascending order of first element of each interval(default behavior)
        # intervals.sort(key=lambda x: x[1]) # sorts in ascending order of 2nd element of each interval
        (start1, end1) = intervals[0]
        for cur_interval in intervals[1:]:
            start2, end2 = cur_interval
            if start2 <= end1:
                # overlapping intervals
                start1, end1 = start1, max(end1, end2)
            else:
                # non overlapping
                merged_intervals.append([start1, end1])
                start1, end1 = start2, end2

        merged_intervals.append([start1, end1])
        return merged_intervals
