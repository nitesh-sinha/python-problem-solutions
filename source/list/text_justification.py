# Given an array of strings words and a width maxWidth, format the text such that each line has exactly
# maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line
# does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots
# on the right.
#
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
#
# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
#
# Example 1:
#
# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
#
# Example 2:
#
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.
#
# Example 3:
#
# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


import math


class TextJustifier:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        line_len = 0
        cur_line_start_idx = 0
        res = []
        last_line = False
        idx = 0
        while idx < len(words):
            # last item is to count number of spaces(1 between each word)
            if len(words[idx]) + line_len + (idx - cur_line_start_idx) <= maxWidth:
                if idx == len(words)-1:
                    last_line = True
                    line_len += len(words[idx])
                    justified_line = self.get_justified_line(words[cur_line_start_idx:], maxWidth, last_line)
                    res.append(justified_line)
                    break
                # Current word can fit in current line
                line_len += len(words[idx])
            else:
                # Current word can't fit in same line
                justified_line = self.get_justified_line(words[cur_line_start_idx:idx], maxWidth, last_line)
                res.append(justified_line)
                # Start a new line
                cur_line_start_idx = idx
                line_len = 0
                idx -= 1
            idx += 1

        return res

    # Given a list of words and maxWidth, this method returns a justified
    # line i.e. either left justified(it is the last line or there is
    # only one word on a non-last line) or full justified otherwise.
    def get_justified_line(self, line_words: list[str], maxWidth: int, last_line: bool) -> str:
        num_words = len(line_words)

        if num_words == 1:
            # left justified singular word
            # Example: 'acknowledgment  '
            return f"{line_words[0]}{' ' * (maxWidth - len(line_words[0]))}"
        elif last_line:
            # left justified words with single space between them
            # and remaining chars after last word filled with spaces
            # Example: 'shall be        '
            non_whitespace_chars = sum(len(word) for word in line_words)
            space_between_words = num_words - 1
            return " ".join(line_words) + " " * (maxWidth - non_whitespace_chars - space_between_words)
        else:
            # fully justified words
            total_chars = sum(len(word) for word in line_words)
            total_spaces = maxWidth - total_chars
            space_slots = num_words - 1

            res = []
            # ALgo ensures that spaces are distributed such that
            # more spaces are assigned between initial words
            # and progressively spaces are reduced as we move to the right
            # Example: 'do  for  you ask'
            for idx, word in enumerate(line_words[:-1]):
                cur_spaces_count = math.ceil(total_spaces / space_slots)
                res.extend([word, " " * cur_spaces_count])
                total_spaces -= cur_spaces_count
                space_slots -= 1

            res.append(line_words[-1])
            return "".join(res)


if __name__ == "__main__":
    tj = TextJustifier()
    print(tj.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    print(tj.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(tj.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
    print(tj.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16))
