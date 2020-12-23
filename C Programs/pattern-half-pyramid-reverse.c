Pattern - Half Pyramid Reverse
Given a positive integer value N as input, print the pattern as in the Example Input/Output section.
Input Format:
The first line contains N.
Output Format:
The pattern as described in the Example Input/Output section.
Boundary Conditions:
2 <= N <= 50
Example Input/Output 1:
Input:
5
Output:
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
Example Input/Output 2:
Input:
6
Output:
6
6 5
6 5 4
6 5 4 3
6 5 4 3 2
6 5 4 3 2 1
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n; scanf("%d",&n);
int i,j;
for(i=n;i>=1;i--)
{
    for(j=n;j>=i;j--)
    {
        printf("%d\t",j);
    }
    printf("\n");
}

}
