Integer - Sum of Digits
The program must accept an integer value N as a command line argument and print the sum of the digits in N.
Example Input/Output 1:
Input:
14
Output:
5
Example Input/Output 2:
Input:
1932
Output:
15'
#include<stdio.h>
int main(int v,char *n[]){
     v=atoi(n[1]);
    int sum=0;
    while(v!=0){
        sum+=v%10;
        v/=10;
    }
    printf("%d",sum);
}
