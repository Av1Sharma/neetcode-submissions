class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        # Sort using a tuple key: (frequency, negative_value)
        nums.sort(key=lambda x: (count[x], -x))
        
        return nums