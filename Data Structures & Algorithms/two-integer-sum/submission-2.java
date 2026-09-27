class Solution {
    public int[] twoSum(int[] nums, int target) {
       for (i=0; i<nums.length; i++){
        a=nums[i]
        for(k=0;k<nums.length;k++){
            b=nums[k]
            if(i!=k&&a+b==target){
                return i,j;
            }
        }
       } 
    }
}
