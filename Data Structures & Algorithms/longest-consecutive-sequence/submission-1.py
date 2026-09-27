class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in seen:
            if num - 1 not in seen:  # beginning of a run
                current = num
                count = 1

                while current + 1 in seen:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest