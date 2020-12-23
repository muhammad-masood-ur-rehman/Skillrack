Pattern - Asterisk Edge
Given a positive integer value N as input, print the pattern as in the Example Input/Output section. The outer edges must be represented by asterisk * and rest by hash #
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
###
###
###

Example Input/Output 2:
Input:
6
Output:
####
####
####
####
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,i,j;
scanf("%d",&n);
for(i=0;i<n;i++)
{
    for(j=0;j<n;j++)
    {   
        if(i==0 || i==n-1)
        {
            printf("*");
        }
        else if(j==0 || j==n-1)
        {
            printf("*");
        }
        else
        {
            printf("#");
        }
    }
    
    printf("\n");
}

}

