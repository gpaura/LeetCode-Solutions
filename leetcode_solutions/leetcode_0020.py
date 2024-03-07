class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:  # len(stack) is 0?
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False
                stack.pop()
        return not stack

# Time Complexity: O(n) where n is the length of the input string
# Space Complexity: O(n) where n is the length of the input string