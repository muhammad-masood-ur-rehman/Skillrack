Longest Palindromic Substring
The program must accept a string S as the input. The program must print the length of longest palindromic substring in the string S as the output.
Boundary Condition(s):
1 <= Length of S <= 10^5
Input Format:
The first line contains the string S.
Output Format:
The first line contains the length of longest palindromic substring in the string S.
Example Input/Output 1:
Input:
sieve
Output:
3
Explanation:
The longest palindromic substring is "eve".
So the length of "eve" is printed as the output.
Example Input/Output 2:
Input:
banana
Output:
5
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        Scanner sc=new Scanner(System.in);
        String str=sc.nextLine();
        int n=str.length(),maxLen=1;
        boolean dp[][]=new boolean[n][n];
        
        for(int i=0;i<n;++i)dp[i][i]=true;
        for(int i=0;i<n-1;++i){
            if(str.charAt(i)==str.charAt(i+1)){
                dp[i][i+1]=true;
                maxLen=2;
            }
        }
        for(int len=3;len<=n;++len){
            for(int i=0;i< n-len+1;++i){
                if(str.charAt(i)==str.charAt(i+len-1) && dp[i+1][i+len-2] ){
                    dp[i][i+len-1]=true;
                    if(len>maxLen)maxLen=len;
                }
            }
        }
        System.out.print(maxLen);
	}
}
