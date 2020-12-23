Number of Ways to Reach Score
Consider a game where a player can score 3 or 5 or 10 points in a move. The program must accept an integer S( total score of the player) as the input. The program must print the number of ways to reach the given score S at any number of moves.
Boundary Condition(s):
1 <= S <= 100000
Input Format:
The first line contains the value of score S.
Output Format:
The first line contains the number of ways to reach the given score at any number of moves.
Example Input/Output 1:
Input:
20
Output:
4
Explanation:
To reach 20 there are 4 ways
10 10
5 5 10
5 5 5 5
3 3 3 3 3 5
Example Input/Output 2:
Input:
5
Output:
1
#include <stdio.h>
#include <stdlib.h>
#define max(x,y) ((x>y)? x:y)

int main()
{
    int num;
    scanf("%d",&num);
    int arr[]={3,5,10};
    int avg[1000000]={1};
    for (int ele=0;ele<3;ele++){
        for(int foo=arr[ele];foo<=num;foo++){
            avg[foo]+=avg[foo-arr[ele]];
        }
    }
    printf("%d",avg[num]);
}
