class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        
        remainder = n % 2

        return remainder + self.hammingWeight(n // 2)

