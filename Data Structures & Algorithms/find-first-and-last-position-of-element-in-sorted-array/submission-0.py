class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find first occurrence
        left = 0
        right = len(nums) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                first = mid
                right = mid - 1   # keep looking LEFT


        # Find last occurrence
        left = 0
        right = len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                last = mid
                left = mid + 1    # keep looking RIGHT

        return [first, last]