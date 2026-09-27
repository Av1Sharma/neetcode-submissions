class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = {
        }

        for num in nums:
            result = hmap.get(num, 0) + 1
            hmap[num] = result
        
        arr = []
        for key, vals in hmap.items():
            if hmap[key] > len(nums) / 3:
                arr.append(key)
        return arr


        