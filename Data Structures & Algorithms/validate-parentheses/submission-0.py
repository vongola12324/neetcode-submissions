class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for ch in s:
            if ch in ["(", "{", "["]:
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != mapping[ch]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
