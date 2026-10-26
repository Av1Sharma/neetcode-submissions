class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        placer = 0

        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[placer]
                nums[placer] = temp
                placer +=1
            print(nums)
        return placer

        