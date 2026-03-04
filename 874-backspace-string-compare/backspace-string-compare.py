class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        stack_1 = []
        stack_2 = []
        
        # Process string s
        for char in s:
            if char == '#':
                if stack_1:
                    stack_1.pop()
            else:
                stack_1.append(char)
        
        # Process string t
        for char in t:
            if char == '#':
                if stack_2:
                    stack_2.pop()
            else:
                stack_2.append(char)
        
        return stack_1 == stack_2