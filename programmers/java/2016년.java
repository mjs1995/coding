class Solution {
    public String solution(int a, int b) {
        int totalDay = 0;
        String[] Dayofweek = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
        for(int i =1 ; i<a; i++){
            if(i ==4 || i == 6 || i ==9 || i ==11 ){
                totalDay += 30;
            } else if (i ==2 ) {
                totalDay += 29;
            } else {
                totalDay += 31;
            }
        }
        totalDay += b+4;
        return Dayofweek[totalDay%7];
        
    }
}
