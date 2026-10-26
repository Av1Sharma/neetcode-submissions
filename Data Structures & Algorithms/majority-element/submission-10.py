class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        
        for key in hashmap.keys():
            if hashmap[key] > len(nums) / 2:
                return key
        