Matrix Zig-Zag from Top Right
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Boundary Condition(s):
1 <= N <= 50
Input Format:
The first line contains the value of N.
Output Format:
The first N lines containing the desired pattern as shown in the Example Input/Output section.
Example Input/Output 1:
Input:
4
Output:
4 3 2 1
5 6 7 8
12 11 10 9
13 14 15 16
Example Input/Output 2:
Input:
3
Output:
3 2 1
4 5 6
9 8 7
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,i,j,number=1,matrix[50][50];
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        if(i==0||i%2==0)
        {
            for(j=n-1;j>=0;j--)
            {
                matrix[i][j]=number;
                number++;
            }
        }
        else
        {
            for(j=0;j<n;j++)
            {
                matrix[i][j]=number;
                number++;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%d ",matrix[i][j]);
        }
        printf("\n");
    }
    return 0;
}
