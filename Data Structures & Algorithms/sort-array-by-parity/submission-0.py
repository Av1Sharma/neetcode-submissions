class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        tracker = 0

        for explorer in range(len(nums)):
            ##this is the excat same thing as move zeros

            if nums[explorer] % 2 == 0:
                nums[tracker], nums[explorer] = nums[explorer], nums[tracker]
                tracker +=1
        return nums        