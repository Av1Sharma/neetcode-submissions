class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:


        for i in range(1, len(nums)):
            a = nums[i]
            b = nums[i-1]

            if a == b or a % 2 == 0 and b % 2 == 0 or a % 2 != 0 and b % 2 !=0:
                return False
        return True
