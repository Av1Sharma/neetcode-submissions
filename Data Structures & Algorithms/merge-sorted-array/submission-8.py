class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        indexToChange = m + n - 1
        lastInums1, lastInums2 = m-1, n-1

        while lastInums2 >= 0:
            if lastInums1 >= 0 and nums1[lastInums1] > nums2[lastInums2]:
                nums1[indexToChange] = nums1[lastInums1]
                lastInums1 -=1
            else:
                nums1[indexToChange] = nums2[lastInums2]
                lastInums2 -=1
            indexToChange -=1
        


        