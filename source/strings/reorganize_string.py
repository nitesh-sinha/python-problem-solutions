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

# Time complexity: O(k* log k) where k=no. of unique chars in input string
# Space complexity: O(k) ignoring the space for result

from heapq import heappush, heappop, heapify
from collections import Counter


class StringReorganizer:
    def reorganize(self, input_str) -> str:
        char_counts_dict = Counter(input_str)
        char_counts_heap = [(-val, key) for key, val in char_counts_dict.items()]
        heapify(char_counts_heap)  # Transform the list to a heap O(k) where k=no. of unique chars in input
        result_str = ""
        while len(char_counts_heap) > 0: # this runs O(k) times
            (big_val, big_key) = heappop(char_counts_heap) # O(1)
            big_val = -1 * big_val
            if len(char_counts_heap) == 0:
                if big_val > 1:
                    # Not possible to form alternate chars string
                    return "Not Possible"
                else:
                    result_str += big_key
                    return result_str
            # Pop next higher count char
            (small_val, small_key) = heappop(char_counts_heap) # O(1)
            small_val = -1 * small_val
            result_str += (big_key + small_key)
            if big_val - 1 > 0:
                heappush(char_counts_heap, (-1 * (big_val - 1), big_key)) # O(log k)
            if small_val - 1 > 0:
                heappush(char_counts_heap, (-1 * (small_val - 1), small_key)) # O(log k)

        return result_str


if __name__ == "__main__":
    org = StringReorganizer()
    print(org.reorganize("aab"))
    print(org.reorganize("aabbcc"))
    print(org.reorganize("aaab"))



# Approach 2(get all permutations for repeated elements in input. Stop as soon as the expected result is found
# Time complexity: O(k*k!) where k=no. of chars in input string. Recursive function is called k! times as kPk = k!
# Space complexity: O(k)
# Inefficient for larger inputs
# class StringReorganizer:
#     def reorganize(self, input_str) -> str:
#         input_chars = list(input_str)
#         input_chars.sort()
#         temp = []
#         found = [False]
#         res = []
#         used = [False for char in input_chars]
#         self.get_permutations(input_chars, temp, res, used, found)
#         if found[0]:
#             return ''.join(res[-1])
#         return "Not Possible"
#
#
#     def get_permutations(self, input_chars: list, temp: list, res: list, used: list, found):
#         if found[0]:
#             return
#         if len(temp) == len(input_chars) and not self.is_adjacent_chars_repeating(temp):
#             found[0] = True
#             res.append(temp.copy())
#             return
#
#         for idx in range(len(input_chars)):
#             if used[idx] or (input_chars[idx - 1] == input_chars[idx] and not used[idx - 1]):
#                 continue
#
#             temp.append(input_chars[idx])
#             used[idx] = True
#             self.get_permutations(input_chars, temp, res, used, found)
#             temp.pop()
#             used[idx] = False
#
#
#     def is_adjacent_chars_repeating(self, temp) -> bool:
#         for idx in range(len(temp)):
#             if idx > 0 and temp[idx] == temp[idx - 1]:
#                 return True
#         return False