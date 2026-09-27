class Solution {
    public boolean hasDuplicate(int[] nums) {
      for (int i=0, i<4,i++){
        int a = nums[i];
        for(int k=1, k<4, k++){
            int b = nums[k];
            if(a==b){
                return false;
            }

        }

      }
      return true;
    }
}