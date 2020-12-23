Pattern Printing – Floyd Triangle
A number N is passed as the number of rows in Floyd’s triangle is passed as the input.  The program must print the Floyd’s triangle pattern.
Example 1:
Input:
7
Output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
n=int(input())
a=1
for i in range(n+1):
    for j in range(0,i):
        print(a ,end=" ")
        a=a+1

    print()
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n;
scanf(“%d”,&n);
int num=1;
int row=1;

while(row <= n)
{
int rowcount=1;

while(rowcount <= row)
{
printf(“%d “,num++);
rowcount++;
}
printf(“\n”);
row++;
}
}
