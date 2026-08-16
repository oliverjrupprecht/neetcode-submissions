class Solution {
    public int[] twoSum(int[] nums, int target) {
        // map : num -> index
        // if map.contains target - current then brilliant 
        if (nums.length == 2) return new int[]{0,1};
        int[] ret = new int[2];
        Map<Integer, Integer> numToIndex = new HashMap<>();
        Integer wantedNum;

        for (int i = 0; i < nums.length; i++) {
            wantedNum = target - nums[i];

            if (numToIndex.containsKey(wantedNum)) { 
                ret[0] = numToIndex.get(wantedNum);
                ret[1] = i;

                return ret;
            } 

            numToIndex.put(nums[i], i);
        }

        return ret;
    }
}
