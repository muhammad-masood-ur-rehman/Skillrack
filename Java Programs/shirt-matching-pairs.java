Shirt - Matching Pairs
A shop to increase sales during a festival has an offer that a customer will get a discount if the customer buys shirts having same size in pairs. Any customer who buys will choose N shirts and the size of the shirt is denoted by S(i) where 1 <= i <=N. Two shirts S(i) and S(j) are matching and form a pair only if S(i) = S(j). The program must print the number of pairs eligible for the discount.

Input Format: The first line will contain the value of N The second line will contain the the size of N shirts S(1) to S(N) with each size separated by a space.

Output Format: The first line will contain the number of matching pairs eligible for the discount.
Constraints: 2 <= N <= 100
Example Input/Output 1:
Input: 9 10 20 20 10 10 30 44 10 20
Output: 3
Explanation: The matching pairs are (10,10) (20,20) (10,10).
Example Input/Output 2:
Input: 642 44 40 42 44 42
Output:2
Explanation: The matching pairs are (42,42) (44,44)
#include<stdio.h>
#include <stdlib.h> 
int main()
{
int r=0,n,c;
scanf("%d",&n);
int a[n],i,b[100];
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
b[i]=-1;
}
for(i=0;i<n;i++)
{
    c=1;
    for(j=i+1;j<n;j++)
    {
        if(a[i]==a[j])
        {
           c++;
           b[j]=0;
        }
    }
    if(b[i]!=0)
    b[i]=c;
}
for(i=0;i<n;i++)
{
    if(b[i]>1)
    r+=b[i]/2;
}
printf("%d",r);

}
import java.util.*;
public class Hello {

    public static void main(String[] args) {
                        Scanner s=new Scanner(System.in);
                        int n=s.nextInt();
                        int[] a=new int[n];
                        int i,j,d=0;
                        for(i=0;i<n;i++){
                        a[i]=s.nextInt();
                        }
        Arrays.sort(a);
                        for(i=0;i<n-1;i++){
                          if(a[i]==a[i+1]){
                          d++;
                          i++;
                          }
                        }
System.out.println(d);
            }
}
