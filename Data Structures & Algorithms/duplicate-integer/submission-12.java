class Solution {
    public boolean hasDuplicate(int[] nums) {
      for (int i=0; i<3; i++){
        int a = nums[i];
        for(int k=1;  k<3;  k++){
            int b = nums[k];
            if(a==b){
                return false;
            }

        }

      }
      return true;
    }
}