Nature of Digit in Position
Given a number ‘n’ and a position; Write an algorithm and subsequent ‘C’ program to Check if the ‘p-th’ Digit, Starting from left-most digiit of the number of the number ‘n’ is ‘odd’ or ‘even’.For most example , if ‘n’ is 3145782 and p is 4 then you have to check if 5 is odd or even. Since it is odd, print ‘Odd’. Make your code to accept numbers of large size.
Input Format:
The first line contains the number, n
The second line contains the position, p
Output Format:
Print either ‘Odd’ or ‘Even’
#include<stdio.h>
void main()
{
    int n;
    int a[100],p,c=0;
    scanf("%d%d",&n,&p);
    while(n>0)
    {
        a[c++]=n%10;
        n=n/10;    }
    if(a[c-p]%2==1)
    printf("Odd");
    else printf("Even");
}
