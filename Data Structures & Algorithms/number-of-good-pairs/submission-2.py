class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        res = 0

        for num in nums:
            if num not in count:
                count[num] = 0

            res += count[num]
            count[num] += 1

        return res