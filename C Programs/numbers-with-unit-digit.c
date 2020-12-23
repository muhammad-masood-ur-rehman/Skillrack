Numbers with Unit Digit
Numbers with Unit Digit
Given two positive integers A and B and a digit U, the program must print all the integers from A to B (inclusive of A and B), which have their unit digit as U.
Input Format:
The first line contains A The second line contains B.The third line contains U.
Output Format:
The first line contains the integers from A to B having their unit digit as U in ascending order with each integer separated by a space.
Boundary Conditions:1 <= A,B <= 99999 0 <= U <= 9
Example Input/Output 1:
Input:
202 103
Output:
23 33 43 53 63 73 83 93 103 113 123 133 143 153 163 173 183 193 203
#include<stdio.h>
int main()
{
int a,b,c;
scanf("%d %d %d",&a,&b,&c);
for(;a<=b;a++){
    if(a%10==c)  
printf("%d ",a);
}
}
