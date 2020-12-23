Integer with Two Digits
The program must accept an integer N as the input. The program must print YES if the integer N is formed using exactly two digits. Else the program must print NO as the output.
Example Input/Output 1:
Input:
57755
Output:
YES
Explanation:
The integer 57755 is formed using exactly two digits 5 and 7.
Hence the output is YES
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
int index,count=0,hash[10]={0};
char input[9];
scanf("%s",input);
for(index=0;index<strlen(input);index++)
{
    hash[input[index]-'0']++;
    if(hash[input[index]-'0']==1)
    count++;
}
if(count==2)
printf("YES");
else
printf("NO");
}
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,c=0;
    scanf("%d",&n);
    int hash[10]={0};
    
    while(n){
        if(hash[n%10]==0){
            c++;
        }
        hash[n%10]++;
        n=n/10;
    }
    printf(c==2? "YES":"NO");
}
C++:
#include <iostream>
 
using namespace std;

int main()

{
    int n,c=0;
    cin>>n;
    int a[10]={0};
    int i;
    while(n)
    {
        if(a[n%10]==0)
        {
            c++;
        }
        a[n%10]++;
        n/=10;
    }


    cout<<(c==2? "yes":"no");


}
Python:
num=int(input());st=[]
while(num>0):
    as=n%10
    st.append(as)
    num//=10
if len(list(set(st)))==2:print("YES")
else:print("NO")
num=input().strip()
if len(set(num))==2:
   print("YES")
else:
   print("NO")
num=list(input())
if len(set(num))==2:
   print("YES")
else:
   print("NO")
