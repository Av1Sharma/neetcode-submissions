class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        left = 0
        right = len(s) -1
        error = 0
        while left < right and error <= 1:
            if s[left] != s[right]:
                error +=1
                left +=1
                right -=1
            else:
                left +=1
                right -=1

            
        return error <= 1