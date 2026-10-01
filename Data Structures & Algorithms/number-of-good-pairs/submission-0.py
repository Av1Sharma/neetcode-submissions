class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        ## could do this in n^2

        ## has to be better way right?
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count+=1

        return count
        
        