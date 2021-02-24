import java.util.*;

class Solution {
    public int[] solution(long n) {
        int[] answer = {};
        ArrayList<Integer>arr = new ArrayList<Integer>();
        long a = 0;
            
        while(n!=0) {
            a = n % 10;
            arr.add((int)a);
            n = n/10;
        }
        
        answer = new int[arr.size()];
        
        for(int i=0; i<arr.size(); i++) {
            answer[i] = arr.get(i);
        }
        return answer;
    }
}
