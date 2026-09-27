class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tracker = 0

        for reader in range(len(nums)):
            if nums[reader] != val:
                nums[tracker], nums[reader] = nums[reader], nums[tracker]
                tracker +=1

        return tracker