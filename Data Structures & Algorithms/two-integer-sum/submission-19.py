class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set(nums)

        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in seen:
                return [i, nums.index(tar)]
        