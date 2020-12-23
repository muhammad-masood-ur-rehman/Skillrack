2D Matrix - Elements Adjacent Sum
Given a matrix of R rows and C columns, for each element print the sum of the adjacent elements.Input Format:The first line contains RThe second line contains CNext R lines each contains C values separated by a spaceOutput Format:R lines each containing C values which represent the sum of the adjacent elements.
Boundary Conditions:
2 <= R,C <= 501 <= Matrix Elements <= 100
Example Input/Output 1:
Input:
5 5
11 11 5 6 18
12 4 16 9 19
5 20 7 5 2
20 19 7 2 11
16 18 5 16 17
Output:
11 16 17 23 6
4 28 13 35 9
20 12 25 9 5
19 27 21 18 2
18 21 34 22 16
#include<stdio.h>
#include <stdlib.h>
int main()
{
int r,c,i,j;
scanf("%d %d",&r,&c);
int a[r][c];
for(i=0;i<r;i++){
    for(j=0;j<c;j++)
    scanf("%d",&a[i][j]);
}
for(i=0;i<r;i++){
    for(j=0;j<c;j++){
        if(j==0) printf("%d ",a[i][j+1]);
        else if(j==c-1) printf("%d ",a[i][j-1]);
        else printf("%d ",a[i][j-1]+a[i][j+1]);
    }
    printf("\n");
}
