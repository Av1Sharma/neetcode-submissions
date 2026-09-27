class Solution {
    public boolean hasDuplicate(int[] nums) {
      for (int i=0; i<nums.length; i++){
        int a = nums[i];
        for(int k=0;  k<nums.length;  k++){
            int b = nums[k];
            if(i!=k&&a==b){
                return true;
            }

        }

      }
      return false;
    }
}