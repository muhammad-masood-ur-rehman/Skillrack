Even Length Substring - Equal Sum Halves [Zoho]
Even Length Substring - Equal Sum Halves: Given a string S as input which consists only of digits from 0 to 9, print the longest substring such that the sum of the digits in the first half and the second half is the same. Print -1 if such a substring does not exist.
Input Format:
The first line contains S
Output Format:
The first line contains the longest substring as per the rules defined above or -1.
Boundary Conditions:
1 <= Length of S <= 100
Example Input/Output 1:
Input:
123123
Output:
123123
Explanation:
The first half is 123 and the second half is 123. Hence the sum of the digits is equal.
Example Input/Output 2:
Input:
1538024
Output:
5380
Explanation:
The first half is 53 and the second half is 80. The sum of the digits is 8 in both the halves.
Example Input/Output 3:
Input:
12345
Output:
-1
Example Input/Output 4:
Input:
989898989
Output:
98989898
Explanation:
Here both 98989898 and 89898989 are of same length. But due to order of occurrence 98989898 is printed as the output.
s=input().strip()
p=[]
r=[s[i:j] for i in range(len(s)) for j in range(len(s)+1) if len(s[i:j])%2==0]
for i in r:
    k=len(i)//2
    a=i[:k];b=i[k:]
    x=0;y=0
    for j in a:
        x+=int(j)
    for h in b:
        y+=int(h)
    if x==y and i!="":
        p.append(i)
if len(p)!=0:
    print(max(p,key=len))
else:
    print(-1)
#include<stdio.h>
#include <stdlib.h>

int main()
{
    char str[100];
    scanf("%s",str);
    
    int l=strlen(str);
    int countrt=0;
    for(int len=l&1? l-1: l;len>=2;len-=2){
        int mid=len/2;
        for(int s=0;s<=l-len;++s){
            int s1=s,num1=0,num2=0;
            int s2=s+mid;
            for(int k=0;k<mid;++k){
                num1+=(str[s1+k]-'0');
                num2+=(str[s2+k]-'0');
            }
            if(num1==num2){
                countrt=1;
                for(int k=0;k<len;++k)printf("%c",str[k+s1]);
                return;
            }
        }
    }
    printf("-1");
    
    return 1;
}
