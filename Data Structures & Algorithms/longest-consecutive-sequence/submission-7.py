class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        
        for n in numset:
            if n+1 not in numset:
                maxLength = 0
                number = n

                while number in numset:
                    maxLength +=1
                    number -=1

                res = max(maxLength, res)
        return res

        