Increase By Adjacent Difference
Increase By Adjacent Difference: Given N numbers, the program must increment a given number by the absolute difference between it's adjacent cells. Treat the other element as zero for the first and last numbers.
Input Format:
The first line contains N.
The second line contains N numbers separated by space.
Output Format:
The first line contains N numbers incremented as per the given condition.
Boundary Conditions:
2 <= N <= 9999
Value of a given number is from -99999 to 99999
Example Input/Output 1:
Input:
6
-20 10 55 -5 20 -10
Output:
-10 85 70 30 25 10
n=int(input())
l=list(map(int,input().split()))
li=[i for i in l]
for i in range(len(l)):
    if i==0:
        li[i]=l[i]+abs(l[i+1]);
    elif i==len(l)-1:
        li[i]=l[i]+abs(l[i-1])
    else:
        li[i]=l[i]+abs(l[i+1]-l[i-1])
for i in li:
    print(i,end=" ")
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,i,d;
scanf("%d", &n);
int a[n];
for(i=0;i<n;i++)
scanf("%d",&a[i]);
int b[n];
for(i=0;i<n;i++)
b[i] = a[i];
for(i=0;i<n;i++)
{
    if(i==0 )
    {
        a[i] = b[i] + abs(b[i+1]);
    }
    else if(i==n-1)
    {
        a[i] = b[i] + abs(b[i-1]);
    }
    else
    {
        d = abs(b[i+1]- b[i-1]);
        a[i] += d;
    }
}

for(i=0;i<n;i++)
printf("%d\t",a[i]);
}
