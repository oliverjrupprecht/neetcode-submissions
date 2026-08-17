class Solution {
    public String longestCommonPrefix(String[] strs) {
        int minLen = Integer.MAX_VALUE;

        for (String s : strs) {
            minLen = Math.min(minLen, s.length());
        }
        
        if (minLen == 0) return new String("");

        StringBuilder sb = new StringBuilder();

        char[] sameIndex = new char[strs.length];
        int count;

        for (int i = 0; i < minLen; i++) {
            count = 0;
            for (String s : strs) {
                sameIndex[count] = s.toCharArray()[i];
                count++;
            }

            if (isAllSame(sameIndex)) {
                sb.append(sameIndex[0]);
            } else {
                return sb.toString();
            }
        }

        return sb.toString();
    }

    private boolean isAllSame(char[] in) {
        char compareChar = in[0];

        for (int i = 1; i < in.length; i++) {
            if (in[i] != compareChar) return false;
        }

        return true;
    }
}