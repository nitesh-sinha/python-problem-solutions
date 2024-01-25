# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1
# does not map to any letters.
import time


# letter_map = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz"
#         }
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
#
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


class CombineLetters:
    def get_combo(self, digits: str) -> list[str]:
        letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        if len(digits) == 0:
            return res
        res = list(letter_map[digits[0]])
        for i in range(1, len(digits)):
            res = [letter1+letter2 for letter1 in res for letter2 in letter_map[digits[i]]]

        return res


if __name__ == "__main__":
    combine = CombineLetters()
    print(combine.get_combo("23"))
    print(combine.get_combo("2"))
    print(combine.get_combo(""))
    print(combine.get_combo("678"))