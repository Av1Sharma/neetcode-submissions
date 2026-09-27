class Solution:
    def validPalindrome(self, s: str) -> bool:
        mismatch = 0


        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                mismatch +=1

            left +=1
            right -=1

        return mismatch <=1