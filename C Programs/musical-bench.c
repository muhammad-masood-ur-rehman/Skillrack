Musical Bench
A group of P players are playing musical bench game in which B number of benches are present in a circular fashion and are placed with equal gaps between adjacent benches. Before the game starts, each one of the players are sitting on any one of these benches which is their initial position IP and each player is having his/her unique id ID. Music is played M number of times (M denotes the number of Rounds) with the duration of play varying which is denoted by M(i). Each player takes his/her own time T(i) to move from one bench to another. If the music is played, players keep moving form one bench to another. At the end of the round one of the benches is removed from the game and also the players who are sitting on that bench are eliminated from the game. The program must print the players ID whose are remaining in the game along with their bench number B. If all the players are eliminated in the game print -1. It is assured that when the music is stopped, the duration for which the music is played is a common multiple of T(i) of all players.
Input Format:
First line contains B and P.
Second line contains the players IDs separated by space.
Third line contains T(i) separated by space.
Fourth line contains players initial bench position IP separated by space.
Fifth line contains M (number of rounds or the number of times the music is played).
sixth line contains M(i) separated by space.
Seventh line contains the bench number which is removed after each round (when the music is stopped).
Output Format:
First line contains the list of ids of the players who are not eliminated and their bench number separated by a colon (or contains -1 if all players are eliminated).
Boundary Conditions:
2 <= B, P <= 100
M <= B
Example Input/Output 1:
Input:
10 6
100 200 300 400 500 600
2 3 4 2 5 3
9 8 9 5 2 1
5
60 120 180 60 60
4 5 3 6 7
Output:
100:10 200:9 600:1
Example Input/Output 2:
Input:
6 4
100 200 300 400
2 4 6 2
2 3 5 1
4
48 36 12 24
1 2 3 5
Output:
-1
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int b,p;
    scanf("%d%d",&b,&p);
    
    int id[p];
    for(int i=0;i<p;++i)scanf("%d",&id[i]);
    
    int playersTime[p];
    for(int i=0;i<p;++i)scanf("%d",&playersTime[i]);
    
    int position[p];
    for(int i=0;i<p;++i)scanf("%d",&position[i]);
    
    int rounds;
    scanf("%d",&rounds);
    
    int roundTime[rounds];
    for(int i=0;i<rounds;++i)scanf("%d",&roundTime[i]);
    
    int benchRem[rounds];
    for(int i=0;i<rounds;++i)scanf("%d",&benchRem[i]);
    
    int isBenchRemoved[101]={0};
    
    for(int rnd=0;rnd<rounds;++rnd){
        for(int i=0;i<p;++i){
            if(isBenchRemoved[position[i]])continue;
            int jumps=roundTime[rnd]/playersTime[i];
            int pos=position[i];
            while(jumps>0){
                pos++;
                if(pos==b+1){
                    pos=1;
                }
                if(!isBenchRemoved[pos])jumps--;
            }
            position[i]=pos;
        }
        isBenchRemoved[benchRem[rnd]]=1;
    }
    int counter=0;
    for(int i=0;i<p;++i){
        if(!isBenchRemoved[position[i]]){
            printf("%d:%d ",id[i],position[i]);
            counter=1;
        }
    }
    if(counter==0)printf("-1");
}
