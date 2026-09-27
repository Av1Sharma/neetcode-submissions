class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums) * 2):
            result.append(nums[i % len(nums)])
        return result
