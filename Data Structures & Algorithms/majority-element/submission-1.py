class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hi = {}

        for num in nums:
            hi[num] = hi.get(num, 0) + 1

        max1 = 0
        answer = 0

        for num in hi:
            if hi[num] > max1:
                max1 = hi[num]
                answer = num

        return answer

        