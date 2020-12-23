Sort Numbers - Factor Count
The program must accept N positive integers as the input and sort them based on the factor count (lowest to highest factor count). If two numbers have the same factor count, order based on the value of the numbers in the ascending order.
Input Format: The first line will contain N. The second line will contain N positive integers separated by a space.
Output Format: The first line will contain the N positive integers (separated by a space) ordered by their factor count.
Boundary Conditions: 2 <= N <= 1000
Example Input/Output 1:
Input:
5
18 23 100 1200 45
Output:
23 18 45 100 1200
Example Input/Output 2:
Input:
3
29 11 101
Output:
11 29 101
n,a=int(input()),[]
v=[int(i) for i in input().split()]
for i in v:
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=1
    a.append(c)

c=sorted(list(zip(a,v)))
for i,j in c:

    print(j,end=' ')
#include<stdio.h>
int main()
{
int n,i,j,c=0,t,t1;
scanf("%d",&n);
int a[n],b[n];
for(i=0;i<n;i++)
{
    scanf("%d",&a[i]);
    for(j=1;j<=a[i];j++)
    {
        if(a[i]%j==0)
            c++;
    }
    b[i]=c;
    c=0;
}
for(i=0;i<n-1;i++)
{
    for(j=i+1;j<n;j++)
    {
        if(b[i]>b[j])
        {
            t1=b[i];
            b[i]=b[j];
            b[j]=t1;
            t=a[i];
            a[i]=a[j];
            a[j]=t;
        }
        else if(b[i]==b[j])
        {
            if(a[i]>a[j])
            {
                t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
    }
}
for(i=0;i<n;i++)
    printf("%d ",a[i]);

}
