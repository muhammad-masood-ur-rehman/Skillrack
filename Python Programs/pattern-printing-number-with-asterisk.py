Pattern Printing Number with Asterisk
Pattern Printing Number with Asterisk Program in Python and C languages
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output sections.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains the value of N.
Output Format:
The first 2*N lines contain the desired pattern as shown in the Example Input/Output sections.
Example Input/Output 1:
Input:
4
Output:
1
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1
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
22*23*24*25*26*27*28
16*17*18*19*20*21
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1
Python Program for Pattern Printing Number with Asterisk
n=int(input());k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end='');k+=1
        if j<i-1:print('*',end='')
    print()
k=k-1
for i in range(n,0,-1):
    l=[]
    for j in range(i):
        l.append(k);k-=1 
        if j<i-1:l.append('*')
    for i in l[::-1]:print(i,end='')
    print()
C program for Pattern Printing Number with Asterisk
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,limit=1,var=0;
    scanf("%d",&n);
    for(int i=1;i<=2*n;i++)
    {
        int p=var;
        for(int j=1;j<=limit;j++)
        {
            printf("%d",++p);
            if(j!=limit)
            {
                printf("*");
            }
        }
        if(i<n)
        {
            limit++;
            var=p;
        }
        else if(i>n)
        {
            limit--;
            var=var-limit;
        }
        printf("\n");
    }
    
    return 0;
}
