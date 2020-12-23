Matrix - Sum of Edge Elements
The input elements of R*C matrix is passed as the input (R is the number of rows and C is the number of columns in the matrix. The program must print the sum S of the elements along the edge of the matrix.
Input Format: The first line contains R and C separated by a space.. Next R lines contain C values each, with the values separated by a space.
Output Format: The first line contains S.
Boundary Conditions:
2 <= R, C <= 100
1 <= Matrix Cell Value <= 1000
Example Input/Output 1:
Input:
5 3
1 2 3
4 5 6
7 8 9
5 5 5
2 2 2
Output:48
Example Input/Output 2:
Input:
3 3
100 200 300
400 500 600
700 800 900
Output:
4000
#include<stdio.h>
#include <stdlib.h>
int main()
{
int r,c,i,j,s=0;
scanf("%d%d",&r,&c);
int m[r][c];
for(i=0;i<r;i++)
{
    for(j=0;j<c;j++)
    {
        scanf("%d",&m[i][j]);
        if(i>0&&i<r-1)
        {
            if(j==0||j==c-1)
            s+=m[i][j];
        }
        else
        s+=m[i][j];
    }
}
printf("%d",s);
}
