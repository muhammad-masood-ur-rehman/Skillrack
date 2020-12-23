Interlace odd / even from A to B
Two numbers A and B are passed as input. The program must print the odd numbers from A to B (inclusive of A and B) interlaced with the even numbers from B to A.
Input Format: The first line denotes the value of A. The second line denotes the value of B.
Output Format: The odd and even numbers interlaced, each separated by a space.
Boundary Conditions: 1 <= A <= 9999999 A < B <= 9999999
Example Input/Output 1:
Input:
5
11
Output:
5 10 7 8 9 6 11
Explanation: The odd numbers from 5 to 11 are 5 7 9 11 The even numbers from 11 to 5 (that is in reverse direction) are 10 8 6 So these numbers are interlaced to produce 5 10 7 8 9 6 11
Example Input/Output 2:
Input:
4
14
Output:
14 5 12 7 10 9 8 11 6 13 4
Explanation: The odd numbers from 4 to 14 are 5 7 9 11 13 The even numbers from 14 to 4 (that is in reverse direction) are 14 12 10 8 6 4 So these numbers are interlaced to produce 14 5 12 7 10 9 8 11 6 13 4 (Here as the even numbers count are more than the odd numbers count we start with the even number in the output)
Example Input/Output 3:
Input:
3
12
Output:
3 12 5 10 7 8 9 6 11 4
Explanation: The odd numbers from 3 to 12 are 3 5 7 9 11 The even numbers from 12 to 3 (that is in the reverse direction) are 12 10 8 6 4 So these numbers are interlaced to produce 3 12 5 10 7 8 9 6 11 4
#include<stdio.h>
int main()
{
int i,n,m,j;
scanf("%d%d",&n,&m);
for(i=n,j=m;i<=m;i++,j--)
{
    if(i%2==1)
    printf("%d\t",i);
    if(j%2==0)
    printf("%d\t",j);
}
}
