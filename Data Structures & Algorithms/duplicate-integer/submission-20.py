class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            seen.append(num)

            if num in seen:
                return True
        return False