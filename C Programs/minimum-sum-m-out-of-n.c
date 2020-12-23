Minimum Sum – M out of N
Given N positive integers, find the minimum sum S that can be obtained by adding exactly M out of the N integers. The program must print the value of the minimum sum S.
Example 1:
Input:
5 2
9 2 1 5 4
Output:
3
Explanation :
Out of the five given numbers, the sum of 1+2=3 is the least sum and hence printed as the output
#include<stdio.h>
#include <stdlib.h>

int main()
{
 int m,n,input[1000],sum=0;
 scanf("%d%d",&m,&n);
 for(int i=0;i<m;i++)
 scanf("%d",&input[i]);
 
 for(int i=0;i<m;i++)
 {
 for(int j=0;j<m;j++)
 {
 if(input[i]<input[j])
 {
 int temp = input[i];
 input[i]=input[j];
 input[j]=temp;
 }
 
 }
 }
 
 for(int i=0;i<n;i++)
 sum=sum+input[i];
 printf("%d ",sum);

}
