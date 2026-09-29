class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            # Pair is correct, single must be to the right
            if nums[mid] == nums[mid + 1]:
                left = mid + 2

            # Pair is broken, single is at mid or to the left
            else:
                right = mid

        return nums[left]