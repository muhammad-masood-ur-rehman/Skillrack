Stair Climbing Combinations
Stair Climbing Combinations: An integer M representing the number of steps in a stair and N sorted integers representing the number of steps can be crossed in each leap are given as the input to the program. The program must print the number of combinations of leaps to climb the stair.
Boundary Condition(s):
1 <= M, N <= 1000
Input Format:
The first line contains M and N separated by space(s).
The second line contains N integers separated by space(s).
Output Format:
The first line contains the number of combinations of leaps to climb the stair.
Example Input/Output 1:
Input:
10 3
2 3 5
Output:
4
Explanation:
The number of combinations to climb 10 stairs are:
{2, 2, 2, 2, 2}
{5, 5}
{2, 3, 2, 3}
{2, 3, 5}
Example Input/Output 2:
Input:
20 4
2 4 6 8
Output:
23
Max Execution Time Limit: 2000 millisecs
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int steps,num;
    scanf("%d %d\n",&steps,&num);
    int arr[num];
    for(int ele=0;ele<num;ele++){
        scanf("%d ",&arr[ele]);
    }
    
    int dp[num+1][steps+1];
    for(int ele=0;ele<steps+1;ele++){
        dp[0][ele]=0;
    }
    for(int ele=0;ele<num+1;ele++){
        dp[ele][0]=1;
    }
    dp[0][0]=0;
    
    for(int ele=1;ele<=num;ele++)
    {
        for(int step=1;step<=steps;step++)
        {
            dp[ele][step]=dp[ele-1][step];
            if((step-arr[ele-1]) >=0){
                dp[ele][step]+=dp[ele][step-arr[ele-1]];
            }
        }
    }
    printf("%d",dp[num][steps]);
    return 0;
}
