class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left+1] == nums[left]:
                left +=2
            else:
                return nums[left]
            if nums[right-1] == nums[right]:
                right -=2
            else:
                return nums[right]
        return 0
            
        