class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        word = Counter(text)
        balloon = Counter("balloon")

        res = 100000
        for c in balloon:
            res = min(res, word[c] // balloon[c])
        
        return res
        

        
        