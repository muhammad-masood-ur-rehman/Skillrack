Pattern Printing - Diamond Numbers
Given an integer N as the input, print the pattern as given in the Example Input/Output section.
Input Format: The first line contains N.
Output Format: 2N-1 lines containing the desired pattern.
Boundary Conditions:
2 <= N <= 50
Example Input/Output 1:
Input:
3
Output:
0 0 1 0 0
0 2 0 8 0
3 0 0 0 7
0 4 0 6 0
0 0 5 0 0
Example Input/Output 2: Input:
5
Output:
0 0 0 0 1 0 0 0 0
0 0 0 2 0 16 0 0 0
0 0 3 0 0 0 15 0 0
0 4 0 0 0 0 0 14 0
5 0 0 0 0 0 0 0 13
0 6 0 0 0 0 0 12 0
0 0 7 0 0 0 11 0 0
0 0 0 8 0 10 0 0 0
0 0 0 0 9 0 0 0 0
C:
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n,i,j,a=0,r=0,k,h;
scanf("%d",&n);
r=2*(2*n-2);
k=((2*n-1)/2)-1;
h=k+2;
for(i=0;i<2*n-1;i++)
{
    for(j=0;j<2*n-1;j++)
    {
        if(i==0)
        {
            if(j==k+1)
                printf("%d ",++a);
            else
                printf("0 ");
        }
        else
        {
            if(j==k+1)
                printf("%d ",++a);
            else if(j==h-1)
                printf("%d ",r--);
            else
                printf("0 ");
        }
    }
    if(i<n-1)
    {
        k--;
        h++;
    }
    else
    {
        k++;
        h--;
    }
    printf("\n");
}


}
