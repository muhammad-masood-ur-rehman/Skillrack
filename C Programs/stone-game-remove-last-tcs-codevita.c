Stone Game - Remove Last - TCS CodeVita
Alice and Bob are playing a game called "Stone Game". Stone game is a two-player game. Let N be the total number of stones. In each turn, a player can remove 1, 2 or 3 stones. The player who picks the last stone, loses. They follow the "Ladies First" norm. Hence Alice is always the one to make the first move. Your task is to find out whether Alice can win, if both play the game optimally.
Input Format:
First line starts with T, which is the number of test cases. Each test case will contain N which represents the number of stones.
Output Format:
Print "Yes" in the case Alice can win, else prints "No".
Boundary Conditions / Constraints:
1<= T <=10
1<= N <=10000

Example Input/Output 1:
Input:
2
1
3

Output:
No
Yes
Explanation:
The first line in the input contains 2 which indicates the number of test cases.
When N=1, Alice will be the first to pick and as there is only one stone, it will be the last pick too. Hence she loses.
When N=3, Alice will pick 2 stones and hence Bob must pick the last stone and she wins.
#include<stdio.h>
int main()
{
    int t,n;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        printf("%s\n",((n%4)==1)?"NO":"YES");
    }
}
