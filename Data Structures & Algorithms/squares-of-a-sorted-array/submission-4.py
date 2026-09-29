class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        indexToPlace = len(nums) - 1
        res = [0] * len(nums)


        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                res[indexToPlace] = nums[left] ** 2
                left +=1
            elif nums[right] ** 2 > nums[left] **2:
                res[indexToPlace] = nums[right] ** 2
                right -=1
            indexToPlace -=1
        return res

