class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dict = {}


        for num in nums:
            result = dict.get(num, 0) + 1
            dict[num] = result
        

        for key, value in dict.items():
            if value > (len(nums) / 2):
                return key


        