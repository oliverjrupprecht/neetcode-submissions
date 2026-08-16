class Solution {
    public int[] getConcatenation(int[] nums) {
        int newLen = 2 * nums.length;
        int[] ans = new int[newLen];

        for (int i = 0; i < newLen; i++) {
            ans[i] = nums[i % nums.length];
        }

        return ans;
    }
}