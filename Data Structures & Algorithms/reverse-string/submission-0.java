class Solution {
    public void reverseString(char[] s) {
        int front = 0;
        int back = s.length - 1;

        char temp;
        while (front < back && front < s.length && back > 0) {
            temp = s[front];
            s[front] = s[back];
            s[back] = temp;
            front++; back--;
        }
    }
}