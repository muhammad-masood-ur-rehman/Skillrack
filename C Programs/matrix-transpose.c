Matrix Transpose
Given a matrix of R rows and C columns as the input, the program must print the transpose of the input matrix.
Input Format:
The first line contains R and C separated by a space.
Output Format:
C lines containing R values each, with the values separated by a space.
Boundary Conditions:
1 <= R, C <= 1000
Example Input/Output 1:
Input:
4 3
62 9 88
72 81 31
3 99 72
3 64 51
Output:
62 72 3 3
9 81 99 64
88 31 72 51
Example Input/Output 2:
Input:
3 3
1 2 3
4 5 6
7 8 9
Output:
1 4 7
2 5 8
3 6 9
#include<stdio.h>
int main()
{
int m,n,i,j;
scanf("%d %d",&m,&n);
int a[m][n];
for(i=0;i<m;i++)
{for(j=0;j<n;j++)
scanf("%d",&a[i][j]);
}
for(j=0;j<n;j++){
    for(i=0;i<m;i++){
        printf("%d ",a[i][j]);
    }
    printf("\n");
}

}
