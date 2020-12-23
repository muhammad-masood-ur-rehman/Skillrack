Browsing Center Computers
In a browsing center, the owner accepts the next day's browsing slot booking from N customers via internet. Each browsing slot contains the start time and the end time in 24-hr format. The browsing center owner must have at least M computers so that no one is waiting. The browsing solt of N customers are passed as the input. The program must print the minimum number of computers M so that no one is waiting in the center.
Boundary Condition(s):
1 <= N <= 10^5
Input Format:
The first line contains N.
The next N lines, each containing the start time and the end time of a browsing slot.
Output Format:
The first line contains M.
Example Input/Output 1:
Input:
6
9:00 11:00
9:30 10:30
9:30 12:00
9:45 13:00
11:00 15:00
10:00 14:00
Output:
5
Explanation:
The browsing center owner must have at least 5 computers so that no one is waiting.
At 10:00, there must be at least 5 computers.
Example Input/Output 2:
Input:
6
9:00 15:00
10:00 10:30
11:00 13:00
13:00 14:00
14:30 15:00
14:30 16:00
Output:
3
#include<stdio.h>
#include <stdlib.h>

int comp(int* a,int* b){
    return *a - *b;
}
int main()
{  
    int n;
    scanf("%d",&n);
    
    int start[n],end[n];
    for(int i=0;i<n;++i){
        int hr,min;
        
        scanf("%d:%d",&hr,&min);
        start[i]=(hr*60)+min;
        
        scanf("%d:%d",&hr,&min);
        end[i]=(hr*60)+min;
    }
    
    qsort(start,n,sizeof(int),comp);
    qsort(end,n,sizeof(int),comp);
    
    int i=0,j=0,maxComp=0;
    
    while(i<n && j<n){
        int presentComp=abs(i-j)+1;
        if(presentComp>maxComp)maxComp=presentComp;
        
        if(start[i]<end[j]){
            i++;
        }
        while(j<n && end[j]<=start[i]){
            j++;
        }
    }
    printf("%d",maxComp);
    
}
