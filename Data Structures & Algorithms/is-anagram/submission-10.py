class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hmap = {}


        for i in range(len(s)):
            result = hmap.get(s[i], 0) + 1
            hmap[s[i]] = result

        for i in range(len(t)):
            if t[i] in hmap:
                hmap[t[i]] -=1
            else:
                return False
        
        for keys, vals in hmap.items():
            if vals > 0:
                return False
        return True
        