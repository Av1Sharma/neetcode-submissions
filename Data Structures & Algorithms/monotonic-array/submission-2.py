class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False
        for i in range(1, len(nums)):
            if decreasing == True and nums[i] > nums[i-1]:
                return False
            if increasing == True and nums[i] < nums[i-1]:
                return False  

            if nums[i] > nums[i-1]:
                increasing = True
            if nums[i] < nums[i-1]:
                decreasing = True

             
        return True
        