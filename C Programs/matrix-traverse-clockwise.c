Matrix Traverse Clockwise
A square matrix of size N*N is provided. The program must traverse the matrix spirally and print the elements in a single line.
Input Format:
The first line contains N.Next N lines, contain N column values C(i,j) each separated by a space.
Output Format:
The first line contains N*N values separated by a space.
Boundary Conditions:
2 <= N <= 1000 <= C(i,j) <= 9999
Example Input/Output 1:
Input:
2
1 2
3 4
Output:
1 2 4 3
Example Input/Output 2:
Input:
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
Example Input/Output 3:
Input:
5
2 7 7 7 9
10 2 4 2 10
2 9 4 9 2
7 15 10 14 10
12 9 15 12 2
Output:
2 7 7 7 9 10 2 10 2 12 15 9 12 7 2 10 2 4 2 9 14 10 15 9 4
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n,i,j,t=0,k=0,z=0;
scanf("%d",&n);
int a[n][n];
for(i=0;i<n;i++){
    for(j=0;j<n;j++)
    scanf("%d",&a[i][j]);
}
if(n%2==0) t=n/2;
else t=n/2+1;
while(k<t){
    i=k;
    for(j=k;j<n;j++)
    printf("%d ",a[i][j]);
    j--;
    for(i=k+1;i<n;i++)
    printf("%d ",a[i][j]);
    i--;
    for(j=i-1;j>=z;j--)
    printf("%d ",a[i][j]);
    //printf("\nhii%d %d",i,j);
    i--;
    j++;
    for(;i>z;i--)
    printf("%d ",a[i][j]);
    k++;
    n--;
    z++;
}

}
