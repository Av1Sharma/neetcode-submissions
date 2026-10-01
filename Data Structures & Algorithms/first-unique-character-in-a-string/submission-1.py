class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1

        hash1 = {}

        for char in s:
            result = hash1.get(char, 0) + 1
            hash1[char] = result


        for key, vals in hash1.items():
            if vals == 1:
                return s.index(key)
        return res
        