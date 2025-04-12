# You are given an array of strings tokens that represents an arithmetic expression in a 
# Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

import math
class ReversePolishNotation:
    # Time complecity: O(n)
    # Space complexity: O(n)
    def evalRPN(self, tokens: list[str]) -> int:
        def perform_operation(operator:str, num1: int, num2: int) -> int:
            match operator:
                case "+":
                    return num1 + num2
                case "-":
                    return num1 - num2
                case "*":
                    return num1 * num2
                case "/":
                    res = num1 / num2
                    res = math.ceil(res) if res<0 else math.floor(res)
                    return res
                case _:
                    return 0
        
        token_stack = []
        valid_operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in valid_operators:
                token_stack.append(int(token))
            else:
                num2 = token_stack.pop()
                num1 = token_stack.pop()
                token_stack.append(perform_operation(token, num1, num2))
        
        return token_stack.pop()
