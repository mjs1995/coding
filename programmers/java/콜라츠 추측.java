class Solution {
    public int solution(int num) {
        int answer = 0;
        int a = num;
        
        while(a != 1 && answer != 500) {
            if(a%2 == 0) {
                a = a/2;
            } else if (a %2 == 1) {
                a = (a*3) + 1;
            }
            answer++;
        }
        if (answer == 500) {
            answer = -1;
        }
            
        return answer;
    }
}
