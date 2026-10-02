class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currentSum = 0
        best = float("inf")

        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum >= target:
                best = min(best, right - left + 1)

                currentSum -= nums[left]
                left += 1

        if best == float("inf"):
            return 0

        return best