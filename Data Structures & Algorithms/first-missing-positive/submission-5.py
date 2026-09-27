class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min1 = min(nums)
        max1 = max(nums)
        notinarr = 0
        
        if max1 <= 0:
          return 1
        seen = set(nums)

        for i in range(1, max1+2):
         if i not in seen:
             return i
        return notinarr

