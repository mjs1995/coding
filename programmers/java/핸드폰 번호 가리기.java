class Solution {
    public String solution(String phone_number) {
        String answer = "";
        String[] a = phone_number.split("");
        for(int i=0; i<a.length; i++) {
            if (i < (a.length -4 )) {
                answer += "*";
            } else {
                answer += a[i];
            }
        }
        return answer;
    }
}
