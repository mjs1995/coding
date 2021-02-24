class Solution {
    public String solution(String s, int n) {
        String answer = "";
        char[] s2 = new char[s.length()];
        
        for(int i=0; i<s2.length; i++){
            s2[i] = s.charAt(i);
        }
        
        for(int i=0; i<s2.length; i++) {
              if(s2[i]==' ') {
                continue;
            } else if(s2[i] >='a' && s2[i] <= 'z') {
                if(s2[i] + n >'z') {
                    s2[i] = (char)(s2[i]+n-26);
                } else {
                    s2[i] += n;
                }
            } else if(s2[i]>= 'A' && s2[i] <= 'Z') {
                if(s2[i]+n > 'Z') {
                    s2[i] = (char)(s2[i]+n-26);
                } else {
                    s2[i] += n;
                }
            }
        }
        
        for(int i=0; i<s2.length; i++ ) {
            answer += s2[i] ;
        }
        return answer;
    }
}
