Two Digits Numbers Sum
Accept an array of N values and print the sum S of all the two digit numbers present in the array. If there are no two digit numbers, print 0.
Input Format:
First line contains the size N
Second line contains N values seperated by a space
Output Format:
The first line contains S.
Boundary Condition:
1 < N < 1000
Example Input/Output 1:
Input:
5
23 898 6 54 21
Ouput:
98
Example Input/Output 2:
Input:
6
231 898 6 541 2 900
Ouput:
0
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n,i,t=0;
scanf("%d",&n);
int a[n];
for(i=0;i<n;i++)
scanf("%d",&a[i]);
for(i=0;i<n;i++)
if(a[i]>9&&a[i]<100)
t+=a[i];

printf("%d",t);

}
n=int(input())
num=[int(i) for i in input().split()]
l=[j for j in num if 9<j<100]

print(sum(l))
