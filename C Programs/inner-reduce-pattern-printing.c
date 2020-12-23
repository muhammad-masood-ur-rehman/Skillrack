Inner Reduce Pattern Printing
Given a number N, the program must print the pattern as described below.
Input Format: The first line contains the value of the N which represent the number N.
Boundary Conditions: 2 <= N <= 9
Output Format: The pattern as described below in the Example Input/Output
Example Input/Output 1:
Input:
4
Output:
4444444
4333334
4322234
4321234
4322234
4333334
4444444
Example Input/Output 2:
Input:
3
Output:
33333
32223
32123
32223
33333
Example Input/Output 3:
Input:
7
Output:
7777777777777
7666666666667
7655555555567
7654444444567
7654333334567
7654322234567
7654321234567
7654322234567
7654333334567
7654444444567
7655555555567
7666666666667
7777777777777
#include<stdio.h>
int main()
{
int n,i,j,t,k,h,g;
scanf("%d",&n);
t=n;
for(i=0;i<2*n-1;i++)
{
    for(j=0;j<2*n-1;j++)
    {
        if(i<n)
        {
            if(i==j)
            {
                for(k=j;k<2*n-i-1;k++)
                    printf("%d",n-i);
                for(g=2*n-i-1;g<2*n-1;g++)
                    printf("%d",++t);
                j=g;
            }
            else
                printf("%d",t--);
        }
        else
        {
            for(h=0;h<2*n-i-1;h++)
                printf("%d",t--);
            ++t;
            for(k=2*n-i-1;k<i+1;k++)
                printf("%d",t);
            for(g=i+1;g<2*n-1;g++)
                printf("%d",++t);
            j=g;
        }
    }
    t=n;
    printf("\n");
}

}
