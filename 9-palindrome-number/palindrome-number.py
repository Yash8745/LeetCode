class Solution:
    def isPalindrome(self, x: int) -> bool:
        if abs(x)!=x:
            return False
        x=str(x)

        if x == x[::-1]:
            return True
        
        return False


        
        