Sum & Product of Digits in N
The program must accept an integer N as the input. The program must find the sum of digits S and the product of digits P in N. Then the program must print yes if the sum of S and P is equal to N. Else the program must print no as the output.
Example Input/Output 1:
Input:
59
Output:
yes
Explanation:
Here N = 59.
The sum of digits in 59 is 14 (5+9 = 14).
The product of digits in 59 is 45 (5*9 = 45).
The sum of 14 and 45 is 59 (14+45 = 59) which is equal to the given integer 59.
So yes is printed as the output.
Here are various methods & Logics 
C++ :
#include <iostream>

int main() {
    using namespace std;
    int num;
    cin>>num;
    int rep=num,sum=0,pro=1;
    while (num>0){
        sum=sum+(num%10);
        pro=pro*(num%10);
        num/=10;
    }
    if((sum+pro)==rep)
    cout<<"yes";
    else
    cout<<"no";
}
Python:
def sumpro(n):
    s1=0;s=0;p=1
    while n>0:
        r=n%10
        s+=r
        p*=r
        n//=10
    s1=p+s
    return s1
n=int(input())
b=sumpro(n)
if b==n:
    print("yes")
else:
    print("no")
a=input().strip()
b=0;c=1 
for i in a:
    b+=int(i)
    c*=int(i)
if b+c==int(a):
    print("yes")
else:
    print("no")
C :
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,sum=0,p=1,dup;
    scanf("%d",&n);
    dup=n;
    while(n>0){
        sum+=n%10;
        p*=n%10;
        n/=10;
    }
    if(dup==sum+p)
    printf("yes");
    else
    printf("no");
}
