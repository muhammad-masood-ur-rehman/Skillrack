Arithmetic Progression – Nth term
The first three terms in an arithmetic progression are passed as input. A positive integer value N (where N > 3) is also passed as the input. The program must print Nth term in the arithmetic.
Example 1:
Input:
5 10 15
6
Output:
30
Explanation:
The progression is 5 10 15 20 25 30 35 so on….
The 6th term is 30.
#include<stdio.h>
#include <stdlib.h>

int main()
{
int arr[10],n;
for(int i=0;i<3;i++)
scanf(“%d”,&arr[i]);
scanf(“%d”,&n);
int diff=arr[1]-arr[0];
int res=arr[0]+(n-1)*diff;
printf(“%d”,res);

 

}
