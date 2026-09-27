class Solution:
    def sortColors(self, nums: List[int]) -> None:

        for writer in range(len(nums)):

            min_index = writer

            for i in range(writer + 1, len(nums)):
                if nums[i] < nums[min_index]:
                    min_index = i

            nums[writer], nums[min_index] = nums[min_index], nums[writer]