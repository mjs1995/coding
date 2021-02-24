import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        ArrayList<Integer> a1 = new ArrayList<Integer>();
        
        int temp = -1;
        for ( int i : arr) {
            if(temp == i) {
            } else {
                a1.add(i);
                temp = i;
            }
        }
        answer = new int[a1.size()];
        
        for (int k =0; k<a1.size(); k++) {
            answer[k] = a1.get(k);
        }
        return answer;
    }
}
