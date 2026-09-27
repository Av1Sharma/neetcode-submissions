class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 = set(nums)
        rmax = 0

        for num in nums1:

            if num - 1 not in nums1:

                counter = 1

                while num + counter in nums1:
                    counter += 1

                rmax = max(rmax, counter)

        return rmax
            
        