class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        start = {}


        for i in range(len(s)):
            start[s[i]] = start.get(s[i], 0) + 1
        
        for i in range(len(t)):
            start[t[i]] = start.get(t[i], 0) - 1

        for value in start.values():
            if value != 0:
                return False

        return True