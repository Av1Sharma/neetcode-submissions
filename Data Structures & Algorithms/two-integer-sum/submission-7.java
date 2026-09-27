class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer;
       for (int i=0; i<nums.length; i++){
        a=nums[i];
        for(int k=0;k<nums.length;k++){
            b=nums[k];
            if(i!=k&&a+b==target){
               answer = new int[]{a,b};
               return answer; 
            }
        }
       } 
    }
}
