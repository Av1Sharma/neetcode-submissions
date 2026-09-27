class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1, hash2 = {}, {}
        for char in s:
            hash1.get(char, 0) + 1

        