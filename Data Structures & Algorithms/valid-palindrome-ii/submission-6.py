class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        error = 0

        while left <= right:
          
            if s[left] != s[right]:
                error +=1
                right -=1
                continue
            
            left +=1
            right -=1

        return error <= 1

