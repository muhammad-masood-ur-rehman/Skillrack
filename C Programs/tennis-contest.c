Tennis Contest
A Tennis contest was scheduled in a college. N number of players registered to participate in this contest. (A player is the winner if he wins in all the rounds of the contest. Every round has elimination. Thus, one-half of the players are eliminated in each round. For example, If P number of players were in a specific round, then P/2 players win and move to the next round). The number of players N and the players details (ID and Name) are given as input. The program should print the names of the players who were defeated by the winner of the contest from final round to the first round.
Note : Total number of players N will always be a power of 2 and N >= 2.
Input/Output Format:
Input:
The first line contains N.
The next N lines contain the player's ID and name separated by a space.
The remaining lines contain the match details in the format WinnerIDvsRunnerID.
Output:
Print the names of the players who were defeated by the winner from final round to the first round.
Example Input/Output 1:
Input:
4
101 Ram
102 Sri
103 Sheik
104 Vel
101vs102
103vs104
101vs103
Output:
Sheik
Sri
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,i,j,k,l=0,m,b[100],c[100],d[100];
char a[100][10];
scanf("%d",&n);
for(i=0;i<n;i++)
{
    scanf("%d%s",&b[i],a[i]);
}
for(i=0;i<n-1;i++)
{
    scanf("%dvs%d",&c[i],&d[i]);
}
for(i=n-2;i>=0;i--)
{
    if(c[i]==c[n-2])
    {
        l=d[i];
        for(j=0;j<n;j++)
        {
            if(l==b[j])
            {
                printf("%s\n",a[j]);
                break;
            }
        }
    }
}
}
