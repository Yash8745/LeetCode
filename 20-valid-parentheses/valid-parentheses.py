class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True

        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in mapping.values():   # opening brackets
                stack.append(ch)
            else:  # closing bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()

        return len(stack) == 0