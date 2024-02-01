from list.merged_intervals import IntervalsMerger

class InsertIntervals:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        idx = 0
        for idx, (cur_start, cur_end) in enumerate(intervals):
            if newInterval[0] > cur_end:
                # new interval is beyond the current interval
                result.append([cur_start, cur_end])
            elif newInterval[1] < cur_start:
                # found the insertion point
                # reduce idx by 1 and append intervals[idx+1:] in L22 so that
                # we don't return last interval for the case when newInterval
                # overlaps with all existing intervals. Check Test case 3 in L33.
                idx -= 1
                break
            else:
                # new interval overlaps with current interval
                # so update the new interval by taking min and
                # max points of the two overlapping intervals
                newInterval[0] = min(newInterval[0], cur_start)
                newInterval[1] = max(newInterval[1], cur_end)

        return result + [newInterval] + intervals[idx+1:]



if __name__ == "__main__":
    ins = InsertIntervals()
    print(ins.insert([[1,3],[6,9]], [2,5]))
    print(ins.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(ins.insert([[1,5],[2,6]], [1,8]))


# Approach 2 (Binary search to get insert_index + insert + merge):
#     def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
#
#         if len(intervals) == 0:
#             return [newInterval]
#
#         insert_idx = self.get_insert_index(intervals, newInterval)
#         merger = IntervalsMerger()
#         return merger.merge(intervals[:insert_idx] + [newInterval] + intervals[insert_idx:])
#
#     def get_insert_index(self, intervals:list[list[int]], new_interval:list[int]) -> int:
#         low, high = 0, len(intervals)
#
#         while low < high:
#             mid = (low + high) // 2
#             if new_interval[0] > intervals[mid][0]:
#                 low = mid + 1
#             else:
#                 high = mid
#
#         return low