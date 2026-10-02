class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for right in range(len(nums)):
            if nums[right] in seen:
                if right - seen[nums[right]] <= k:
                    return True

            seen[nums[right]] = right

        return False