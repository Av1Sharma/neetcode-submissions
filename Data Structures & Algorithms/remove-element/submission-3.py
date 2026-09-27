class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       r = 0
       count = 0



       for i in range(len(nums)):
        if val != nums[i]:
            temp = nums[i]
            nums[i] = nums[r]
            nums[r] = temp
            r +=1 
            count +=1
        
       return count

    

        