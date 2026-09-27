class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num

            # Check if the complement is already in our dictionary
            if complement in seen:
                # We found it! Return the index of the complement and our current index
                return [seen[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[current_num] = i
        
        
        