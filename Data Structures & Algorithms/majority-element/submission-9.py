class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}

        for num in nums:
            result = hmap.get(num, 0) + 1
            hmap[num] = result

        for key, val in hmap.items():
            if hmap[key] > len(nums) / 2:
                return key
        
        