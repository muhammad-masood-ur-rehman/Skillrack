Uncertain Steps - TCS CodeVita
Uncertain Steps: Codu is trying to go down stairs from his building to ground floor. He can go 3 ways.
1) Walk 1 step at a time.
2) Extend his legs and go 2 steps at a time.
3) Jump down 3 steps at a time.
Given N steps, calculate the number of possible ways W to reach the ground floor, provided he can jump 3 steps. That is, he can jump down 3 steps only once, but at any time, if he wishes, while walking down the stairs.
Note: As the number of ways W can be huge, print W modulo 1000000007.
Boundary Condition(s):
1 <= N <= 10^6
Input Format:
The first line contains N.
Output Format:
The first line contains W.
Expample Input/Output 1:
Input:
4
Output:
7
Explanation:
The 7 possible ways are given below.
1, 1, 1, 1
1, 1, 2
1, 2, 1
2, 1, 1
2, 2
1, 3
3, 1
Expample Input/Output 2:
Input:
5
Output:
13
#include <stdio.h>
#include <stdlib.h>
#define ULL unsigned long long int
int main()
{
    ULL sum;
    ULL with[3];
    ULL without[3];
    int i,val=1000000007;
    int N;
    scanf("%d",&N);
    if(N==1){
        printf("-1");
        return 0;
    }
    without[0]=with[0]=1;
    without[1]=with[1]=1;
    without[2]=with[2]=2;
    for(i=3;i<=N;++i){
        sum=with[2]+with[1]+without[0];
        with[0]=with[1];
        with[1]=with[2];
        with[2]=sum%val;
        sum=without[2]+without[1];
        without[0]=without[1];
        without[1]=without[2];
        without[2]=sum%val;
        
    }
    printf("%llu",with[2]);
    return 0;
}
#include<stdio.h>
#include <stdlib.h>

int main()
{
    long long int n;
    scanf("%lld",&n);
    long long int dp1[n+1],dp2[n];
    dp1[0]=1;
    for(int i=1;i<=n;++i){
        dp1[i]=dp1[i-1];
        if(i-2>-1){
            dp1[i]+=dp1[i-2];
        }
        dp1[i]=dp1[i]%1000000007;
    }
    for(int i=0;i<=n;++i){
        if(i<=2){
            dp2[i]=dp1[i];
        }
        else{
            dp2[i]=dp2[i-1]+dp2[i-2]+dp1[i-3];
        }
        dp2[i]=dp2[i]%1000000007;
    }
    printf("%lld",dp2[n]%1000000007);
    
    return 0;
}
