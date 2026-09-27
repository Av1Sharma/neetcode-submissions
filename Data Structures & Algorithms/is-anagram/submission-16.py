class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1 = {}


        for char in s:
            hash1[char] = hash1.get(char, 0) + 1


        for char in t:
            if char in hash1:
                hash1[char] -=1
            else:
                return False
        for key, val in hash1.items():
            if val > 0:
                return False
        return True
        