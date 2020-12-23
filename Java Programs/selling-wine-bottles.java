Selling Wine Bottles
There are N wine bottles packed and arranged in a row from left to right. The wine bottles can be sold only one per year with a condition that only the leftmost or the rightmost wine bottle can be sold. The price of a wine bottle P(i) where 1 <= i <= N (which has not been sold yet) increases by it's initial price P(i) every year. Find the maximum revenue that can be obtained by selling the wine bottles based on the above conditions.
Boundary Condition(s):
1 <= N <= 10^6
1 <= P(i) <= 100
Input Format:
The first line contains N.
The second line contains N integers representing the price of the wine bottles separated by a space.
Output Format:
The first line contains the maximum revenue that can be obtained by selling the wine bottles based on the above conditions.
Example Input/Output 1:
Input:
4
1 4 2 3
Output:
29
Explanation:
Max revenue =  1*1 + 3*2 + 2*3 + 4*4 = 29
Example Input/Output 2:
Input:
5
3 5 7 3 6
Output:
79
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        int arr[]=new int[n];
        
        for(int i=0;i<n;++i)arr[i]=scan.nextInt();
        
        int dp[][]=new int[n][n];
        
        System.out.print(getans(arr,dp,0,n-1,1));
	}
	public static int getans(int arr[],int dp[][],int left,int right,int year){
	    if(dp[left][right]!=0){
	        return dp[left][right];
	    }
	    if(left==right){
	        return arr[left]*year;
	    }
	    int leftrevenue=arr[left]*year + getans(arr,dp,left+1,right,year+1);
	    int rightrevenue=arr[right]*year + getans(arr,dp,left,right-1,year+1);
	    dp[left][right]=Math.max(leftrevenue,rightrevenue);
	    return dp[left][right];
	}
}
