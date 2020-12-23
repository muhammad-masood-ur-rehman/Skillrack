Largest Possible Odd Integer
The program must accept an integer N as the input. The program must print the largest possible odd integer using all the digits in N as the output. If it is not possible to form such an integer, the program must print no as the output.
Boundary Condition(s):
10 <= N <= 10^17
Input Format:
The first line contains N.
Output Format:
The first line contains the largest possible odd integer using all the digits in N or no.
Example Input/Output 1:
Input:
120087460153
Output:
876543210001
Explanation:
The largest possible odd integer using all the digits in 120087460153 is 876543210001.
Example Input/Output 2:
Input:
246228
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
    int lastDigit=1;
    while(lastDigit<10 && hash[lastDigit]==0)lastDigit+=2;
    if(lastDigit>9){
        printf("no");
        return;
    }
    hash[lastDigit]--;
    
    int firstDigit=9;
    while(firstDigit>0 && hash[firstDigit]==0){
        firstDigit--;
    }
    if(firstDigit==0){
        printf("%d",lastDigit);
        return;
    }
    hash[firstDigit]--;
    
    printf("%d",firstDigit);
    for(int i=9;i>-1;--i)while(hash[i]--)printf("%d",i);
    printf("%d",lastDigit);
    return;
}
