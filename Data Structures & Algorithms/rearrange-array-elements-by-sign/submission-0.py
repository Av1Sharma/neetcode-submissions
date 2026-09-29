class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        postracker, negtracker = 0, 1

        ## why? positive numbers will forever be at even indexes, negative numbers at odds

        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                res[postracker] = nums[i]
                postracker +=2
            else:
                res[negtracker] = nums[i]
                negtracker +=2
        return res

        ##holy shit no way first try



        
        