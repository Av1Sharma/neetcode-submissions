class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        spointer = 0
        tpointer = 0

        if t in s:
            return 0
        while spointer < len(s):
            print(spointer, tpointer)
            if s[spointer] == t[tpointer]:
                spointer +=1
                tpointer +=1
            else:
               spointer +=1
            if tpointer == len(t):
                return 0

        return len(t[tpointer:])
        
            
