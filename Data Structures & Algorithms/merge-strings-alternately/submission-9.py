class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        wrd1 = 0 
        wrd2 = 0
        
        final = ""

        while wrd1 < len(word1) and wrd2 < len(word2):
            final += word1[wrd1]
            final += word2[wrd2]

            wrd1 +=1
            wrd2 +=1

        if len(word1) > len(word2):
            final += word1[wrd1:]

        if len(word2) > len(word1):
            final += word2[wrd2:]
        
        return final 
        