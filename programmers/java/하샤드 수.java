class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        int x1 = x;
        while (x1>0) {
            sum += x1 % 10;
            x1 = x1 /10;
        }
        if(x%sum != 0) {
            answer = false;
        }
        return answer;
    }
}
