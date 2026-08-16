class Solution {
    public int[] twoSum(int[] nums, int target) {
        // map : num -> index
        // if map.contains target - current then brilliant 
        if (nums.length == 2) return new int[]{0,1};

        Map<Integer, Integer> numToIndex = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            Integer wantedNum = target - nums[i];

            if (numToIndex.containsKey(wantedNum)) { 
                return new int[]{numToIndex.get(wantedNum),i};
            } 

            numToIndex.put(nums[i], i);
        }

        return new int[]{};
    }
}
