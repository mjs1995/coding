class Solution {
  public long solution(long n) {
	      long answer = 0;
	      
	      if((long)Math.sqrt(n) * (long)Math.sqrt(n) == n) {
	    	  answer = ((long)Math.sqrt(n) + 1) * ((long)Math.sqrt(n) +1);
	      } else {
	    	  answer = -1;
	      }; 
	      
	      return answer;
  }
}
