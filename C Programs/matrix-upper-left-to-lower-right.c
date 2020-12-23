Matrix - Upper Left to Lower Right
The program must accept the upper left triangle elements of an integer matrix size of NxN as the input. The program must fill the lower right triangle of the matrix with the inverted upper left triangle elements. Finally, the program must print the modified matrix as the output. 
Boundary Condition(s): 2 <= N <= 100 
Input Format: 
The first line contains the value of N. 
The next N lines contain the upper left triangle elements separated by space(s). 
Output Format: 
The first N line contain N elements of the modified matrix separated by space(s). 
Example Input/Output 1: 
Input: 
4 3 7 3 7 3 2 8 4 8 9
Output 
3 7 3 7 3 2 8 3 4 8 2 7 9 4 3 3 
Explanation: 
The upper left triangle elements are 
3 7 3 7 3 2 8 4 8 9 
The inverted upper left trianlge (lower right triangle) elements are 
* * * 7 * * 8 3 * 8 2 7 9 4 3 3 
Now the elements in the matrix are 
3 7 3 7 3 2 8 3 4 8 2 7 9 4 3 3 
Example Input/Output 2: 
Input: 
5 37 11 37 18 37 62 29 32 58 62 91 75 80 11 53 
Output: 
37 11 37 18 37 62 29 32 58 18 62 91 75 32 37 80 11 91 29 11 53 80 62 62 37
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,i,j;
    scanf("%d",&n);
    int m[n][n],mat[n][n];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n-i;j++)
        {
            scanf("%d",&m[i][j]);
            mat[i][j]=m[i][j];
        }
    }
    for(i=0;i<n;i++)
    {
        int t=i;
        for(int p=i;p<i+1;p++)
            for(int k=0;k<n-i;k++)
            printf("%d ",m[p][k]);
        for(j=0;j<i;j++)
        {
            printf("%d ",mat[--t][n-i-1]);
        }
        printf("\n");
    }

}
