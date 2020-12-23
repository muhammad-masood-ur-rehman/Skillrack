Social Media Leader
There are N people in a Facebook group.
The group follows the following three rules.
1) The group leader does not follow anyone.
2) Everyone in the group follows the group leader.
3) No more than one group leader is allowed.
The N people are numbered from 1 to N. The program must accept the integer N and R relationships.
Each relationship contains two integers representing who follows whom.
The program must print an integer denoting the group leader.
If the group leader can not be found, the program must print -1 as the output.
Example
Input/Output 1:
Input:
5 7
1 3
2 3
3 4
5 3
1 4
5 4
2 4
Output: 4
#include<stdio.h>
#include <stdlib.h>
int main()
{
    int n,r;
    scanf("%d%d",&n,&r);
    
    int followsCount[100000]={0},followersCount[100000];
    
    for(int i=0;i<r;++i){
        int follower,follows;
        scanf("%d%d",&follower,&follows);
        followsCount[follower]++;
        followersCount[follows]++;
    }
    for(int i=1;i<=n;++i){
        if(followersCount[i]==n-1 && followsCount[i]==0){
            printf("%d",i);
            return;
        }
    }
    printf("-1");
    return;
}
