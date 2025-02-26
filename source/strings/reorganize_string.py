# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
#
# Return any possible rearrangement of s or return "Not Possible" if not possible.
#
# Example 1:
#
# Input: s = "aab"
# Output: "aba"
#
# Example 2:
#
# Input: s = "aaab"
# Output: "Not Possible"
#
# Constraints:
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.

from heapq import heappush, heappop, heapify
from collections import Counter


class StringReorganizer:
    def reorganize(self, input_str) -> str:
        char_counts_dict = Counter(input_str)
        char_counts_heap = [(-val, key) for key, val in char_counts_dict.items()]
        heapify(char_counts_heap)  # Transform the list to a heap
        result_str = ""
        while len(char_counts_heap) > 0:
            (big_val, big_key) = heappop(char_counts_heap)
            big_val = -1 * big_val
            if len(char_counts_heap) == 0:
                if big_val > 1:
                    # Not possible to form alternate chars string
                    return "Not Possible"
                else:
                    result_str += big_key
                    return result_str
            # Pop next higher count char
            (small_val, small_key) = heappop(char_counts_heap)
            small_val = -1 * small_val
            result_str += (big_key + small_key)
            if big_val - 1 > 0:
                heappush(char_counts_heap, (-1 * (big_val - 1), big_key))
            if small_val - 1 > 0:
                heappush(char_counts_heap, (-1 * (small_val - 1), small_key))

        return result_str


if __name__ == "__main__":
    org = StringReorganizer()
    print(org.reorganize("aab"))
    print(org.reorganize("aabbcc"))
    print(org.reorganize("aaab"))
