class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}


        for char in s:
            result = hmap.get(char, 0) + 1
            hmap[char] = result

        for char in t:
            if char in hmap:
                hmap[char] = hmap.get(char) - 1
            else:
                return False
        
        for val in hmap.values():
            if val > 0:
                return False

        return True
        