class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(-(stack.pop() - stack.pop()))
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack[0]

# Time Complexity: O(n) where n is the length of the list of tokens
# Space Complexity: O(n) where n is the number of tokens in the list. 
# This worst-case scenario occurs when all tokens are numbers and are thus pushed onto the stack.