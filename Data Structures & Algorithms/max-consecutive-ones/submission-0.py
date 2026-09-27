class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mmax = 0
        lmax = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                lmax +=1
            else:
                mmax = max(mmax, lmax)
                lmax = 0
        mmax = max(mmax, lmax)
        return mmax
        