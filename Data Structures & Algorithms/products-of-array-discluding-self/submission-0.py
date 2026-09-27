class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                prefix[i] *= nums[j]
            for x in range(i+1, len(nums)):
                suffix[i] *= nums[x]
            
        for i in range(len(prefix)):
            prefix[i] = prefix[i] * suffix[i]

        return prefix
            

        


            
            




        