Lucky Number
A Lucky Number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are lucky numbers.
Example: 19 is a lucky number
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Write a program to find whether Nandhini would receive the gift voucher on a particular day. Input is the number of likes that her post received on a particular day.
Business Rules:
Print Invalid Input if the input is negative or if the input is greater than 1000000.
Input Format:
Input consists of an integer that corresponds to the number of likes.
Output Format:
Output consists of a string that is either “YES” or “NO” or “Invalid Input”.
Sample Input 1:
19
Sample Output 1:
YES
Sample Input 2:
20
Sample Output 2:
NO
Sample Input 3:
-20
Sample Output 3:
Invalid Input
#include<stdio.h>
int main()
{
 unsigned int n,t=0,s=0;
 scanf("%d",&n);
 if(n>0&&n<1000000){
 while(n>=9){
     while(n){
     t=n%10;
     t*=t;
     s+=t;
     //printf("%d",s);
     n/=10;
     }
     n=s;
     s=0;
 }
 if(n==1) printf("YES");
 else printf("NO");
 }
 else printf("Invalid Input");
 return 0;
}
