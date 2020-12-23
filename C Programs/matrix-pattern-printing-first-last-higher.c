Matrix Pattern Printing - First / Last Higher
Given an integer N as the input, print the pattern as given in the Example Input/Output section.
Input Format: The first line contains N.
Output Format: N lines containing the desired pattern.
Boundary Conditions:
2 <= N <= 100
Example Input/Output 1:
Input:
3
Output:
1 1 1 2
3 2 2 2
3 3 3 4
#include<stdio.h>
int main()
{
int N;
scanf("%d",&N);
int i,j,a=1;
for(i=0;i<N;i++)
{
    for(j=0;j<=N;j++)
    {
        if(i%2==0)
        {
            if(j==N)
                printf("%d ",a+1);
            else
                printf("%d ",a);
        }
        else
        {
            if(j==0)
                printf("%d ",a+1);
            else
                printf("%d ",a);
        }
    }
    a++;
    printf("\n");
}

}
