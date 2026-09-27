class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            found = False
            for j in range(index, len(nums2)):
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    found = True
                    break
            if found == False:
                res.append(-1)
        return res

        