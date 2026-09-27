class Solution:
    def myPow(self, x: float, n: int) -> float:
        total = 1
        c = 0
        while c < abs(n):
            total *=x 
            c +=1
        if n < 0:
            return 1 / total
        return total
        