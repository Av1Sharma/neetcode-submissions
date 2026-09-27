class Solution:
    def myPow(self, x: float, n: int) -> float:

        total = 1

        for i in range(abs(n)):
            total *= x

        if n < 0:
            return 1 / total

        return total