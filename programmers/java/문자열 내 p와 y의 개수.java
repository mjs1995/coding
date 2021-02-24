class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        s = s.toLowerCase();
        
        String[] s1 = new String[s.length()];
        int[] p_y = {0,0};
        s1 = s.split("");
        
        for(int i=0; i<s1.length; i++) {
            if(s1[i].equals("p")) {
                p_y[0] ++;
            } else if(s1[i].equals("y")) {
                p_y[1] ++;
            }
        }
        
        if(p_y[0] == p_y[1]) {
            answer = true;
        } else {
            answer = false;
        }
        return answer;
    }
}
