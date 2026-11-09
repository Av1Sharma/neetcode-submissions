class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[0 : int(len(nums)/2)]
        nums2 = nums[int(len(nums)/2):]
        res = []
        index = 0
        while len(nums2) > index:
            res.append(nums1[index])
            res.append(nums2[index])
            index +=1

        return res