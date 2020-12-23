Step Numbers from 1 to N
The program must accept an integer N as the input. The program must print all the step numbers from 1 to N as the output. If there is no such integer then the program must print -1 as the output. A number is called a step number if all the adjacent digits have an absolute difference of 1.
Note: The number of digits in a step number is always greater than 1.
Input Format:
The first line contains N.
Output Format:
The first line contains the integer value(s) or -1.
Example Input/Output 1:
Input:
12
Output:
10 12
Explanation:
The absolute difference between all the adjacent digits in the integer 10 is 1 (1 - 0).
The absolute difference between all the adjacent digits in the integer 12 is 1 (1 - 2).
So the step numbers from 1 to 12 are 10 and 12.
Hence the output is 10 12
Example Input/Output 2:
Input:
5
Output:
-1
Example Input/Output 3:
Input:
130
Output:
10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98 101 121 123
C:
#include<stdio.h>
#include <stdlib.h>
int fun(int n){
    while(n/10){
        if(abs(n%10 - (n/10)%10 )!=1)return 0;
        n=n/10;
    }
    return 1;
}
int main()
{
    int n;
    scanf("%d",&n);
    
    int i=10,c=0;
    
    while(i<=n){
        if(fun(i)){
            printf("%d ",i);
            c=1;
        }
        i++;
    }
    if(c==0)printf("-1");
}
Python:
a=int(input());p=0
for i in range(10,a+1):
    d,c=i,0
    while d>9:
        if abs(d%10-(d//10)%10)!=1:
            c=1
            break
        d//=10;
    if c==0:print(i,end=' ');p=1
if p==0:print(-1)
