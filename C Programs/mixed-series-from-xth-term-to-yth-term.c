Mixed Series - From Xth term to Yth term
The program must accept the first four terms of a mixed series and two integers X and Y as the input. The program must print all the terms from Xth term to Yth term as the output. 
Note: The odd terms in the series form an arithmetic progression. The even terms in the series form another arithmetic progression. 
Boundary Condition(s): 
1 <= First four terms in the mixed series <= 10^18 
1 <= X < Y <= 10^8 
Input Format: 
The first line contains the first four terms of the mixed series separated by a space. The second line contains X and Y separated by a space. 
Output Format: 
The first line contains all the terms from Xth term to Yth term separated by a space. 
Example Input/Output 1: 
Input: 
10 20 35 60 
11 15 
Output: 
135 220 160 260 185 
Explanation: 
The 11th term in the mixed series is 135. 
The 12th term in the mixed series is 220. 
The 13th term in the mixed series is 160. 
The 14th term in the mixed series is 260. 
The 15th term in the mixed series is 185. 
Example Input/Output 2: 
Input: 
2 5 4 9 
4 10 
Output: 9 6 13 8 17 10 21
#include<stdio.h>
#include <stdlib.h>
#define llu long long int
int main()
{
    llu m,n,x,y,s,e;
    scanf("%lld%lld%lld%lld%lld%lld",&m,&n,&x,&y,&s,&e);
    llu var1=x-m;
    llu var2=y-n;
    int count=0;
    for(int ele=1;ele<=e;++ele){
        if(ele>=s){
            printf("%lld ",count? n: m);
        }
            if(count){
                n=n+var2;
            }
            else{
                m=m+var1;
            }
            count=!count;
}
    
    return 0;
}
