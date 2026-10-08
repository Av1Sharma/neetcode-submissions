class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for char in s:
            freq = hashmap.get(char, 0) + 1
            hashmap[char] = freq


        len1 = 0
        for key, val in hashmap.items():
            while val >= 2:
                len1 +=2
                val -=2
        if len1 + 1 <= len(s):
            len1 +=1
        return len1

        