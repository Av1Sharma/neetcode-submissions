class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        localSum = nums[0]
        globalSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                localSum += nums[i]
            else:
                localSum = nums[i]

            globalSum = max(globalSum, localSum)

        return globalSum