class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        tracker = 1

        for reader in range(1, len(nums)):

            if nums[reader] != nums[tracker - 1]:
                nums[tracker], nums[reader] = nums[reader], nums[tracker]

                tracker +=1
        return tracker        