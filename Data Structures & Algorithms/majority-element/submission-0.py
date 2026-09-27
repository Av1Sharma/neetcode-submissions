class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hi = {}

        for num in nums:
            hi[num] = hi.get(num, 0) + 1

        max1 = 0
        for num in hi.values():
            max1 = (max1, num)

        return hi.get(num)

        