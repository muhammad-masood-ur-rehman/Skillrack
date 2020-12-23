Perfect Squares - Till N
Given a positive integer N as the input, print all the perfect squares till N (inclusive of N).
Input Format:
The first line contains N.
Output Format:
The first line contains the perfect squares till N separated by a space.
Boundary Conditions:
1 <= N <= 9999999
Example Input/Output 1:
Input:
20
Output:
1 4 9 16
Example Input/Output 2:
Input:
1
Output:
1
#include <stdio.h>
void printSquare(int n)
{
 for(int i=1;i*i<=n;i++)
  printf("%d ",i*i);
}
void main()
{
int N;
scanf("%d",&N);
printSquare(N);
}
