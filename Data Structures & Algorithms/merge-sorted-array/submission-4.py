class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        num1last, nums2last = m - 1, n - 1

        while nums2last >= 0:
            if num1last >= 0 and nums1[num1last] > nums2[nums2last]:
                nums1[last] = nums1[num1last]
                num1last -= 1
            else:
                nums1[last] = nums2[nums2last]
                nums2last -= 1

            last -= 1