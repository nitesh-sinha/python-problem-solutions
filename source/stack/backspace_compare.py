#         Given two strings S and T, return if they are equal when both are typed 
#         into empty text editors. # means a backspace character.
# 
#         Example 1:
# 
#         Input: S = "ab#c", T = "ad#c"
#         Output: true
#         Explanation: Both S and T become "ac".
# 
#         Example 2:
# 
#         Input: S = "ab##", T = "c#d#"
#         Output: true
#         Explanation: Both S and T become "".
# 
#         Example 3:
# 
#         Input: S = "a##c", T = "#a#c"
#         Output: true
#         Explanation: Both S and T become "c".
# 
#         Example 4:
# 
#         Input: S = "a#c", T = "b"
#         Output: false
#         Explanation: S becomes "c" while T becomes "b".
#         Note:
# 
#         1 <= S.length <= 200
#         1 <= T.length <= 200
#         S and T only contain lowercase letters and '#' characters.
# 
#  Time complexity: O(N) where N= sum of chars in S and T
#  Space complexity: O(N)

from collections import deque
class BackspaceComparator:

    def compare(self, str1: str, str2:str) -> bool:
        return self.parse_string(str1) == self.parse_string(str2)

    def parse_string(self, input_str: str) -> str:
        stack = deque()
        for char in input_str:
            if char == '#' and len(stack) > 0:
                stack.pop()
            elif char != '#':
                stack.append(char)

        return ''.join(stack)


if __name__ == "__main__":
    comp = BackspaceComparator()
    print(comp.compare("ab#c", "ad#c"))
    print(comp.compare("ab##", "c#d#"))
    print(comp.compare("a##c", "#a#c"))
    print(comp.compare("a#c", "b"))


