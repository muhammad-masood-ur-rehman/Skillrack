Square Matrix – Corner Elements Sum
A square matrix of size N*N is passed as input. The program must calculateand print the sum of the elements in the corners.
Example 1:
Input:
3
10 90 1
4 22 5
32 8 66
Output:
109
Explanation:
The sum = 10+1+66+32 = 109
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,arr1[1000][1000],sum;
scanf(“%d”,&n);

for(int i=0;i<n;i++)
for(int j=0;j<n;j++)
scanf(“%d”,&arr1[i][j]);

sum=arr1[0][0]+arr1[0][n-1]+arr1[n-1][0]+arr1[n-1][n-1];

printf(“%d”,sum);

}
