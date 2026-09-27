class Solution {
    public boolean hasDuplicate(int[] nums) {
      for (int i=1; i<5; i++){
        int a = nums[i];
        for(int k=2;  k<5;  k++){
            int b = nums[k];
            if(a==b){
                return false;
            }

        }

      }
      return true;
    }
}