class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        groups1 = {}
        groups2 = {}

        for num in nums1:
            groups1[num] = groups1.get(num, 0) + 1
        for num in nums2:
            groups2[num] = groups2.get(num, 0) + 1

        result = []

        for num in groups1:
            if num in groups2:
                result.append(num)

        return result 