class Solution:
    def longestPalindrome(self, s: str) -> int:

        hash1 = {}


        for char in s:
            result = hash1.get(char, 0) + 1
            hash1[char] = result

        count = 0
        for keys, values in hash1.items():
            while values >= 2:
                count +=2
                values -=2
        
        return count + min(1, max(0, len(s) - count)) #this line is so chopped omg lol
                
            
        