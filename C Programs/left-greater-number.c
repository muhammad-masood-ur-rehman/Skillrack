Left Greater Number
Given an array of N positive integers, for each number print the first number to it’s left which is greater than the current number.
Print -1 if there is no greater number on it's left.
Input Format: The first line contains N. The second line contains N space separated positive integers.
Output Format: N integers which represent the left greater numbers separated by a space.
Boundary Conditions:
2 <= N <= 10^6
Example Input/Output 1:
Input:
6 5 3 2 4 8 6
Output:
-1 5 3 5 -1 8
Example Input/Output 2:
Input:
11 3 8 5 11 10 10 3 16 11 12 15
Output:
-1 -1 8 -1 11 11 10 -1 16 16 16
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n,i,j;
scanf("%d",&n);
int a[n];
for(i=0;i<n;i++)
scanf("%d",&a[i]);
for(i=0;i<n;i++)
{
    if(i==0)
    printf("-1");
    else
    {
       for(j=i-1;j>=0;j--)
     {
        if(a[j]>a[i])
       {
        printf("%d ",a[j]);
        break;
       }
       else if(j==0)
       printf(" -1");
      } 
    }   
}

}
