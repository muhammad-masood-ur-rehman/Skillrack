Right Triangle with Asterisk Pattern
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains the integer N.
Output Format:
The first N lines contain the desired pattern as shown in the Example Input/Output section.
Example Input/Output 1:
Input:
4
Output:
1
2*3
4*5*6
7*8*9*10
Example Input/Output 2:
Input:
7
Output:
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
16*17*18*19*20*21
22*23*24*25*26*27*28
Max Execution Time Limit: 2000 millisecs
#include <stdio.h>

int main()
{
    int num,count=1;
    scanf("%d",&num);
    for(int i=0;i<num;i++)
    {
        for(int j=0;j<=i;j++)
        {
            if(j!=0)printf("*");
            printf("%d",count++);
        }
        printf("\n");
    }
    return 0;
}
