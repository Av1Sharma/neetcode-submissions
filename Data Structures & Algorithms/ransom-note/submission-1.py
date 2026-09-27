class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hash1 = {}


        for char in ransomNote:
            result = hash1.get(char, 0) + 1

            hash1[char] = result

        a: 2


        for char in magazine:
            if char in hash1:
                hash1[char] -=1
        for key, val in hash1.items():
            print(key, val)
        for vals in hash1.values():
            if vals > 0:
                return False
        return True