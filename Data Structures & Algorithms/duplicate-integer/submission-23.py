class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsdup = set(nums)


        return len(nums) != len(numsdup)
        
        