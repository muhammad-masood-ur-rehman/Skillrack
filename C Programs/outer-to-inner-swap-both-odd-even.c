Outer to Inner Swap - Both Odd/Even
Outer to Inner Swap - Both Odd/Even
Given N numbers, the program must swap the first and last element,
swap 2nd and last but one element and so on if both the elements are odd or even. If N is odd, the swap will not occur for the middle element.
Input Format:
The first line contains N.
The second line contains N numbers separated by space.
Output Format:
The first line contains N numbers swapped as per the given condition.
Boundary Conditions:
2 <= N <= 9999
Value of a given number is from 1 to 99999
Example Input/Output 1:
Input:
7
4 11 17 6 11 18 2
Output:
2 11 11 6 17 18 4
Explanation:
Take 4 and 2. Swap occurs as both are even.
Now 11 and 18, no swap as 11 is odd and 18 is even.
Now consider the pair 17 and 11. Swap occurs as both are odd.
6 is middle element (as N is odd) and hence retained as it is.
n=int(input())
l=list(map(int,input().split()))
l2=[None for i in range(n)]
for i in range(n//2+1):
    if((l[i]+l[n-i-1])%2==0):
        l2[i]=l[n-i-1]
        l2[n-i-1]=l[i]
    else:
        l2[i]=l[i]
        l2[n-i-1]=l[n-i-1]
for i in l2:
    print(i,end=" ")
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n;
scanf("%d", &n);
int a[n];
int i,j= 0, k = n-1,temp;
for(i=0;i<n;i++)
scanf("%d", &a[i]);

for(i=0;i<n/2;i++)
{
    if((a[k]%2 == 0 && a[j]%2==0) || (a[k]%2!=0 && a[j]%2!=0))
    {
        temp = a[k];
        a[k] = a[j];
        a[j] = temp;
    }
    k--;
    j++;
}

for(i=0;i<n;i++)
printf("%d\t",a[i]);

}
