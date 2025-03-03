# Given a string s, partition the string into one or more substrings such that the characters in each substring are
# unique. That is, no letter appears in a single substring more than once.
#
# Return the minimum number of substrings in such a partition.
#
# Note that each character should belong to exactly one substring in a partition.
#
# Example 1:
# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
#
#
# Example 2:
# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").
#
#
# Constraints:
# 1 <= s.length <= 105
# s consists of only English lowercase letters.

# Time complexity: O(n) where n=length of input string

class MinSubstrings:
    def partition_string(self, s: str) -> int:
        chars_seen = set()
        min_substrings = 1
        for char in s:
            if char in chars_seen:
                # Repeated char found
                # Start a substring
                min_substrings = min_substrings + 1
                chars_seen.clear()
            chars_seen.add(char)
        return min_substrings


if __name__ == "__main__":
    print(MinSubstrings().partition_string("abacaba")) # 4
    print(MinSubstrings().partition_string("ssssss")) # 6
    print(MinSubstrings().partition_string("abacd")) # 2
