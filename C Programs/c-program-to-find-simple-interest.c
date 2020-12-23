C Program to find Simple Interest
The program must accept principal amount P, interest rate R and time period in years N as the input. The program must calculate and print the simple interest value as the output with precision upto decimal places.
Formula: SI = P*N*R/100
Example Input/Output 1:
Input:
10000 12 5
Output:
6000.00
Example Input/Output 2:
Input:
1000 5 2
Output:
100.00
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    int h=(a*b*c);
    float si=(h/100);
    printf("%.2f",si);

}
