Sum of Factorial of Digits
The program must accept an integer N as the input. The program must print the sum of factorial of the digits in N as the output.
Boundary Condition(s):
10 <= N <= 10^17
Input Format:
The first line contains N.
Output Format:
The first line contains the sum of factorial of the digits in N.
Example Input/Output 1:
Input:
147
Output:
5065
Explanation:
1! + 4! + 7! = 1 + 24 + 5040 = 5065
Example Input/Output 2:
Input:
2986
Output:
403922
Python :
import math
num=input().strip()
su=0
for ele in num:
   su=su+math.factorial(int(ele))
print(su)
def recur_factorial(n):
   if n == 1:
       return n
    elif n == 0:
        return 1
   else:
       return n*recur_factorial(n-1)
num=input()
su=0
for ele in num:
    su+=recur_factorial(int(ele))
print(su)
C :
#include<stdio.h>
#include <stdlib.h>

int main()
{
    long long int num,product,sum=0;
    scanf("%lld",&num);
    for(int index1=num;num>0;)
    {
        product=1;
        for(int index=1;index<=num%10;index++)
        {
            product=product*index;
        }
        sum=sum+product;
        num=num/10;
    }
    printf("%lld",sum);

}
#include<stdio.h>
#include <stdlib.h>
int fact(int num){
    int ans=1;
    for(int ele=2;ele<=num;++ele)ans*=ele;
    return ans;
}
int main()
{
    char str[20];
    scanf("%s",str);
    
    int su=0;
    for(int ele=0;ele<strlen(str);++ele){
        su+=fact(str[ele]-'0');
    }
    printf("%d",su);
}
