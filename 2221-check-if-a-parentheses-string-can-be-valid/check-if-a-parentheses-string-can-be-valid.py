class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        s_len = len(s)
        if s_len % 2 != 0:  # If the string length is odd, it's impossible to have balanced parentheses
            return False
        
        stack_locked = []  # Stack to store indices of locked '('
        stack_unlocked = []  # Stack to store indices of unlocked characters ('0')
        
        # Forward pass: Check if it's possible to balance '('
        for i in range(s_len):
            if locked[i] == '0':  # Unlocked character
                stack_unlocked.append(i)
            elif s[i] == "(":
                stack_locked.append(i)
            else:  # Locked ')'
                if stack_locked:  # Try to match with a locked '('
                    stack_locked.pop()
                elif stack_unlocked:  # If no locked '(', try to use an unlocked character
                    stack_unlocked.pop()
                else:  # No '(' to match this ')'
                    return False
        
        # At this point, stack_locked may contain unmatched '('
        # Backward pass: Check if it's possible to balance remaining '(' using unlocked characters
        while stack_locked:
            if not stack_unlocked:  # If there are no unlocked characters left
                return False
            # Ensure unlocked character is after the locked '('
            if stack_locked[-1] > stack_unlocked[-1]:
                return False
            stack_locked.pop()
            stack_unlocked.pop()
        
        return True
