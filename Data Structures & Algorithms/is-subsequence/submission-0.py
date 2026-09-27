class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:


        pointer = 0
        for i in range(len(s)):
            
            while s[i] != t[pointer]:
                if pointer == len(t)-1:
                    return False
                print(pointer)
                pointer +=1
        return True
            



        