Matrix Diagonals Sum
You are given a square matrix of size N*N.Calculate the sum of integers present in the two main diagonals
Example 1:
Input:
3
5 10 11
79 6 12
9 21 45
Explanation:
The sum is 5+6+45+11+9=76.
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,arr[20][20];
scanf("%d",&n);
int sum=0;
for(int i=0;i<n;i++){
for(int j=0;j<n;j++){
scanf("%d",&arr[i][j]);
if(i==j)
sum=sum+arr[i][j];
else if(i+j==(n-1))
sum=sum+arr[i][j];
}
}
printf("%d",sum);

}
