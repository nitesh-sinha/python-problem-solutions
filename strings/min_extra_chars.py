# You are given a 0-indexed string s and a dictionary of words dictionary.
# You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary.
# There may be some extra characters in s which are not present in any of the substrings.
# Return the minimum number of extra characters left over if you break up s optimally.
#
# Example 1:
# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8.
# There is only 1 unused character (at index 4), so we return 1.
#
# Example 2:
#
# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12.
# The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters.
# Hence, we return 3.
#
# Constraints:
#
# 1 <= s.length <= 50
# 1 <= dictionary.length <= 50
# 1 <= dictionary[i].length <= 50
# dictionary[i] and s consists of only lowercase English letters
# dictionary contains distinct words


class MinExtraChars:
    def getMinExtraChars(self, s: str, dictionary: list[str]) -> int:
        length = len(s)
        dp = [0] * (length+1) # dp[i] contains minExtraChars if input string is s[i:]

        start_index, end_index, step = length-1, -1, -1
        for i in range(start_index, end_index, step):
            # To start, we assume that this char will be an extra leftover char
            # hence 1 + minExtraChars when input string is s[i+1:]
            dp[i] = 1+dp[i+1]
            for word in dictionary:
                # For all words in dictionary, check if word from dictionary
                # matches the word created with starting character at i
                if i+len(word)<=length and s[i:i+len(word)] == word:
                    # Word from dictionary matches the word built with start char at i
                    # hence obtain min of extra chars
                    dp[i] = min(dp[i], dp[i+len(word)])

        return dp[0]


if __name__ == "__main__":
    x = MinExtraChars()
    print(x.getMinExtraChars("leetscode", ["leet", "code", "leetcode"]))
    print(x.getMinExtraChars("sayhelloworld", ["hello", "world"]))
