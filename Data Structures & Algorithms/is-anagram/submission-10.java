class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> sMap = new HashMap<>(); 
        Map<Character, Integer> tMap = new HashMap<>(); 

        for (char c : s.toCharArray()) {
            Character C = new Character(c);
            if (sMap.containsKey(C)) {
                sMap.put(C, sMap.get(C) + 1);
            } else {
                sMap.put(C, 1);
            }
        }

        for (char c : t.toCharArray()) {
            Character C = new Character(c);
            if (tMap.containsKey(C)) {
                tMap.put(C, tMap.get(C) + 1);
            } else {
                tMap.put(C, 1);
            }
        }

        return sMap.equals(tMap); 
    }
}
