class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums) * 2):
            if i > 4:
                result.append(nums[i - 4])
                continue
            result.append(nums[i])

        return result


            

