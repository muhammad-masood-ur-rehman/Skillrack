Cyclic Shift
Given a set of elements, write an algorithm and the subsequent ‘C’ program to perform cyclic right shift of the array by 'm' places. For example, if the elements are 12, 13, 16, 7, 10 and m =2 then the resultant set will be 7, 10, 12, 13, 16.
Input Format
Number of elements in 'n'
element1
element2
...
elementn
value of 'm'
Output Format
Elements in the set after right shift by 'm' places
Input:
number of elements n
The n elements
Output:
Elements in the set after right shift by 'm' places
#include< stdio.h >
void main()
{
    int a[20],n,i,m,t,j;
    scanf("%d",&n);
    for(i=0;i < n;i++)
    scanf("%d",&a[i]);
    scanf("%d",&m);
    for(j=0;j < m;j++)
    {
        t=a[n-1]; 
        for(i=n-1;i > 0;i--)
        a[i]=a[i-1];
        a[0]=t;
    }
    for(i=0;i < n;i++)
    printf("%d\n",a[i]);
}
