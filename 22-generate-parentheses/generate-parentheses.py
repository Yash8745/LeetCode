class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []  # This will store the final result
        
        def backtrack(openN, closedN, current):
            # If we've used n opening and n closing parentheses, add to result
            if openN == closedN == n:
                res.append(current)
                return
            
            # If we can still add an opening parenthesis, do so
            if openN < n:
                backtrack(openN + 1, closedN, current + '(')
            
            # If we can still add a closing parenthesis, do so
            if closedN < openN:
                backtrack(openN, closedN + 1, current + ')')
        
        # Start the backtracking with 0 open and 0 closed parentheses
        backtrack(0, 0, '')
        
        return res
