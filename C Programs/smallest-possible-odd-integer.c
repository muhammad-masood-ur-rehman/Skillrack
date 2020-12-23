Smallest Possible Odd Integer
The program must accept an integer N as the input. The program must print the smallest possible odd integer using all the digits in N as the output. If it is not possible to form such an integer, the program must print no as the output.
Boundary Condition(s):
10 <= N <= 10^17
Input Format:
The first line contains N.
Output Format:
The first line contains the smallest possible odd integer using all the digits in N or no.
Example Input/Output 1:
Input:
1670078423
Output:
1002346787
Explanation:
The largest possible odd integer using all the digits in 1670078423 is 1002346787.
Example Input/Output 2:
Input:
40068
Output:
no
#include<stdio.h>
#include <stdlib.h>

int main()
{
    long long int n;
    scanf("%lld",&n);
    int hash[11]={0};
    
    while(n>0){
        hash[n%10]++;
        n=n/10;
    }
    
    int lastDigi=9;
    while(lastDigi>=0 && hash[lastDigi]==0)lastDigi-=2;
    if(lastDigi<0){
        printf("no");
        return;
    }
    hash[lastDigi]--;
    
    int firstdigi=1;
    while(firstdigi<10 && hash[firstdigi]==0)firstdigi++;
    if(firstdigi==10){
        printf("%d",lastDigi);
        return;
    }
    hash[firstdigi]--;
    
    printf("%d",firstdigi);
    
    for(int i=0;i<=9;++i)while(hash[i]--)printf("%d",i);
    
    printf("%d",lastDigi);

}
