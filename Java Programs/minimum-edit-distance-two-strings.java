Minimum Edit Distance Two Strings
The program must accept two string values S1 and S2 as the input.
The program must print the minimum cost required to convert the string S1 to S2 as the output.
The cost of insertion, deletion and substitution of any character in the string S1 will be 1.
Example
Input/Output 1:
Input:
hello
hail
Output:
3
#include<stdio.h>
#include <stdlib.h>
#define min(x,y) x<y? x:y

import java.util.*;
public class Main {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        String s1=scan.nextLine(),s2=scan.nextLine();
        int l1=s1.length(),l2=s2.length();
        int dp[][]=new int[l2+1][l1+1];
        
        for(int i=0;i<=l1;++i)dp[0][i]=i;
        for(int i=0;i<=l2;++i)dp[i][0]=i;
        
        for(int i=1;i<=l2;++i){
            for(int j=1;j<=l1;++j){
                if(s2.charAt(i-1)!=s1.charAt(j-1)){
                    dp[i][j]=Math.min(dp[i-1][j-1],dp[i-1][j]);
                    dp[i][j]=Math.min(dp[i][j],dp[i][j-1])+1;
                }
                else{
                    dp[i][j]=dp[i-1][j-1];
                }
            }
        }
        System.out.print(dp[l2][l1]);
        return;
	}
}
