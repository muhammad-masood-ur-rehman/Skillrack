2D Matrix Absolute Difference Diagonals Elements Sum
A Square Matrix has N rows and N columns. Get the matrix as input and find the absolute difference between the sum of the values in the two diagonals. 
Input Format: The first line contains N. Next N lines containing the elements of the matrix with N column values separated by a space.
Output Format: Absolute difference between the sum of the values in the two diagonals.  
Boundary Conditions:
· 1 <= N <= 100 
Example Input/Output 1: 
Input: 2 35 80 90 20 
Output:115 
Example Input/Output 2: 
Input:4 1 4 4 2 2 2 1 8 8 1 3 5 10 1 8 3 
Output:5
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n,t=0,i,j,d=0;
scanf("%d",&n);
int a[n][n];
for(i=0;i<n;i++){
    for(j=0;j<n;j++){
        scanf("%d",&a[i][j]);
        if(i==j) t+=a[i][j];
        if(i+j==n-1) d+=a[i][j];
    }
}
printf("%d",abs(t-d));

}
n=int(input())
m=[[int(i) for i in input().split()]for j in range(n)]
s=sum(m[i][i]for i in range(n))
s1=sum(m[i][n-i-1]for i in range(n))

print(abs(s-s1))
