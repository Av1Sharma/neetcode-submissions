class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        rnew = []


        for i in range(len(nums) * 2):
            rnew.append(nums[i % len(nums)])
        
        return rnew