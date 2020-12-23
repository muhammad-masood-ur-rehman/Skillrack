Single Source Shortest Path
There are N cities in a country which are numbered from 1 to N.
The N cities are connected by L links. Each link contains the source city,
the destination city and the distance between them.
The program must accept the values of N and L links as the input.
The program must print the shortest distance from the city 1 to all the other cities as the output.
Example
Input/Output 1:
Input:
6 7
1 2 20
1 6 5
6 5 2
5 4 3
4 3 2
5 2 10
3 2 2
Output:
14 12 10 7 5
Explanation:
The shortest distance from the city 1 to 2 is 14 (1 -> 6 -> 5 -> 4 -> 3 -> 2).
The shortest distance from the city 1 to 3 is 12 (1 -> 6 -> 5 -> 4 -> 3).
The shortest distance from the city 1 to 4 is 10 (1 -> 6 -> 5 -> 4).
The shortest distance from the city 1 to 5 is 7 (1 -> 6 -> 5).
The shortest distance from the city 1 to 6 is 5 (1 -> 6).
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,l;
    scanf("%d%d",&n,&l);
    
    int source[l+1],desination[l+1],distance[l+1];
    for(int i=1;i<=l;++i){
        scanf("%d%d%d",&source[i],&desination[i],&distance[i]);
    }
    int ans[n+1];
    ans[1]=0;
    for(int i=2;i<n+1;++i)ans[i]=-1;
    
    int counter=1;
    
    for(int iter=0;iter<n && counter; ++iter)
    {
        counter=0;
        for(int i=1;i<=l;++i){
            int src=source[i],dst=desination[i];
            if(ans[src]==-1){
                continue;
            }
            if(ans[dst]==-1 || ((ans[src]+distance[i]) < ans[dst])){
                counter=1;
                ans[dst]=ans[src]+distance[i];
            }
        }
    }
    for(int i=2;i<=n;++i)printf("%d ",ans[i]);
}
