class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        if t in s:
            return 0

        
        sPointer = 0
        tPointer = 0

        while sPointer < len(s):
            if t[tPointer] == s[sPointer]:
                tPointer +=1
            
            sPointer +=1

        if tPointer != len(t) - 1:
            return len(t) - tPointer
        return 1

