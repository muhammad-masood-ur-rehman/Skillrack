Array Element Adjacent Sum
Given an Array of length N, the program must print the sum of adjacent numbers of elements present in the array.
Input Format:
First line contains N.Second line contains N element values seperated by a space.
Output Format:
Adjacent sum of N elements seperated by a space.
Boundary Conditions:2 <= N <= 100
Example Input/Output 1:
Input:
5
1 1 1 1 1
Output
1 2 2 2 1
Example Input/Output 2:
Input:
10
7 9 3 7 9 1 10 2 9 7
Output:
9 10 16 12 8 19 3 19 9 9
Example Input/Output 3:
Input:
2
1 2
Output:
2 1
#include<stdio.h>
#include <stdlib.h>
int main()
{
int n,i;
scanf("%d",&n);
int a[n];
for(i=0;i<n;i++)
scanf("%d",&a[i]);
for(i=0;i<n;i++){
    if(i==0) printf("%d ",a[i+1]);
    else if(i==n-1) printf("%d ",a[i-1]);
    else printf("%d ",a[i-1]+a[i+1]);
}

}
m=int(input())
n=[int(i) for i in input().split()]
print(n[1],' ',*[n[i-1]+n[i+1] for i in range(1,m-1)],' ',n[m-2]) 
