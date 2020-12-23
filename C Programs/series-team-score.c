Series Team Score
Two soccer team A and B play a series of matches over a period of time. In a match, the winning team gets 3 points. If the match ends in a tie(draw) both tea scoring same goals, then both the team get one point each.  The losing team does not get any point
The program must accept the goals scored by both team A and B in certain number of matches and print the cumulative scores of team A and B separated by a space.
Example 1:
Input:
3 5 1
3 2 0
Output:
7 1
Explanation:
Team A drew the first match and hence both team A and
b got one point each
Team B won both matches two and three and hence got additional 6 points
So the final score of team A is 7 and team B is 1.
#include<stdio.h>
#include <stdlib.h>

int main()
{
int team1[100],team2[100],i=0,k;
int sum1=0,sum2=0;
while(scanf(“%d”,&team1[i] )==1)
i++;

for(int j=0,k=i/2;j<i/2,k<i;j++,k++)
{
if(team1[j]>team1[k])
sum1=sum1+3;
else if(team1[j]==team1[k])
{
sum1=sum1+1;
sum2=sum2+1;
}
else
sum2=sum2+3;
}
printf(“%d %d”,sum1,sum2);

}
