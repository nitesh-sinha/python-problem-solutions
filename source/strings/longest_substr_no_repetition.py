# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class LongestSubstrNoRepetition:
    # ALgorithm 1(Brute force):
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     max_len = 0
    #     char_set = set()
    #     cur_len = 0
    #     for idx_start in range(len(s)):
    #         max_len = max(max_len, cur_len)
    #         char_set.add(s[idx_start])
    #         cur_len = 1
    #         for idx_end in range(1+idx_start, len(s)):
    #             if s[idx_end] not in char_set:
    #                 char_set.add(s[idx_end])
    #                 cur_len += 1
    #             else:
    #                 char_set.clear()
    #                 break
        
    #     # if no repetition seen until end of s
    #     max_len = max(max_len, cur_len)
    #     return max_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Algorthm 2: Sliding window, hash table to stop char latest positions
        # Time complexity: O(n)
        # Space complexity: O(n)
        char_pos_map = {}
        char_pos_map = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] in char_pos_map and char_pos_map[s[right]] >= left:
                # current char seen earlier and is part of the current substring, 
                # so reset the substring by excluding the earlier seen cur character
                left = char_pos_map[s[right]] + 1

            char_pos_map[s[right]] = right
            max_len = max(max_len, right-left + 1)

        return max_len
