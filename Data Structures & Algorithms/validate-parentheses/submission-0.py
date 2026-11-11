class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in brackets_map:
                top = stack.pop() if stack else 'q'
                if brackets_map[char] != top:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0