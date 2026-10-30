class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i2 = 0
        i = 0

        while i < len(nums1) and i2 < len(nums2):
            if nums1[i] == 0:
                nums1[i] = nums2[i2]
                i2 +=1
            i +=1

        nums1.sort()
        
            
        