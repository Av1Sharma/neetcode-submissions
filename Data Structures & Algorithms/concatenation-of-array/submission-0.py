class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [0] * len(nums) * 2

        ansC = 0
        while ansC < len(ans):
            for i in range(len(nums)):
                ans[ansC] = nums[i]
                ansC +=1
        return ans


            
        