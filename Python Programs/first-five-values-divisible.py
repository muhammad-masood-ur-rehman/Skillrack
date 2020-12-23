First Five Values Divisible
Three numbers A, B and C are passed as input. The program must print the first five values that are divisible by A, B and C.
Input Format:
The first line denotes the value of A.
The second line denotes the value of B.
The third line denotes the value of C.
Output Format:
The first line contains the first five numbers divisible by A, B and C (with each value separated by a space).
Boundary Conditions:
1 <= A <= 9999
1 <= B <= 9999
1 <= C <= 9999
Example Input/Output 1:
Input:
2
3
4
Output:
12 24 36 48 60
Example Input/Output 2:
Input:
4
6
8
Output:
24 48 72 96 120
#include<stdio.h>
#include <stdlib.h>
int main()
{
int a,b,c,i,f=0;
scanf("%d%d%d",&a,&b,&c);
for(i=1;i<1000;i++){
    if(f==5)
    break;
    if(i%a==0&&i%b==0&&i%c==0){
    printf("%d ",i);
    f++;
    }
}
 }
from fractions import gcd
d=[int(input()),int(input()),int(input())]
l=d[0]
for i in d:
    l=l*i//gcd(l,i)
i=1
while i!=6:
    print(l*i,end=" ")

    i+=1
