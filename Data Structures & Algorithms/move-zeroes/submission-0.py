class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ## we need a tracker to keep where the next 0 to replace is


        tracker = 0

        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[tracker], nums[explorer] = nums[explorer], nums[tracker]
                tracker +=1

        return nums
        