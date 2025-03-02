# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
# Time complexity: O(n^2) where n=length of input string

class LongestPalindrome:
    def get_palindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_palin = ""

        # expand_and_get_palindrome expands along the string given
        # left and right indices until it can find a palindromic
        # substring.
        # Returns the longest palindromic substring centred around
        # starting left and right indices
        def expand_and_get_palindrome(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # exclude chars at current left and right
            # as they're unequal or beyond the length of string
            return s[left + 1:right]

        for i in range(len(s)):
            # find both odd length and even length palindromes
            # (even length palindrome calculation is needed to account
            # for these cases: s = "aaaab")
            odd_len_palin = expand_and_get_palindrome(i, i)
            even_len_palin = expand_and_get_palindrome(i, i + 1)
            if len(odd_len_palin) > len(max_palin):
                max_palin = odd_len_palin
            if len(even_len_palin) > len(max_palin):
                max_palin = even_len_palin
        return max_palin


if __name__ == "__main__":
    lp = LongestPalindrome()
    print(lp.get_palindrome("abbad"))
    print(lp.get_palindrome("aa"))
    print(lp.get_palindrome("a"))
    print(lp.get_palindrome(""))
    print(lp.get_palindrome("aaaab"))
    print(lp.get_palindrome("abcd"))


# Algorithm 2 (Time complexity: O(n^3) where n=length of given string):
# def get_palindrome(self, s: str) -> str:
#     for idx in range(len(s), 0, -1):
#         # Extract idx length strings and check if its palindrome
#         for start in range(len(s) - idx + 1):
#             extracted_str = s[start: start+idx]
#             if self.is_palindrome(extracted_str):
#                 return extracted_str
#
# def is_palindrome(self, s: str) -> bool:
#     start, end=0, len(s)-1
#     while start < end:
#         if s[start] != s[end]:
#             return False
#
#         start+=1
#         end-=1
#     return True