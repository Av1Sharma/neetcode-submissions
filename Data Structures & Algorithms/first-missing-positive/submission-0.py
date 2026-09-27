class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min1 = min(nums)
        max1 = max(nums)

        hash1 = {}

        for num in nums:
            result = hash1.get(num, 0) + 1
            hash1[num] = result
        arr = []
        for key, val in hash1.items():
            arr.append(key)
        
        for i in range(min1, max1):
            if i not in arr:
                return i
        return max1 + 1



        