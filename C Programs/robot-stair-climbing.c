Robot - Stair Climbing
There are N stairs to be climbed in a building. A robot can take only S different leaps each containing certain distinct steps which are passed as the input. The program must print the number of ways C of steps the robot can take to climb exactly N stairs.
Boundary Condition(s):
1 <= N <= 50
1 <= S <= 10
Input Format:
The first line contains N and S separated by a space.
The second line contains S integer values separated by a space.
Output Format:
The first line contains the C.
Example Input/Output 1:
Input:
5 2
2 3
Output:
2
Explanation:
There are 5 steps. The robot can take 2 or 3 steps at a time.
So the possible ways are
2 3 and 3 2
Example Input/Output 2:
Input:
6 2
1 5
Output:
3
Explanation:
The possible ways are
1 1 1 1 1 1
5 1
1 5
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int x,y;
    scanf("%d%d",&x,&y);
    int array[x];
    for(int i=0;i<x;i++)scanf("%d",&array[i]);
    x++;
    y++;
    int arr[x][y];
    for(int i=0;i<x;i++){
        for(int j=0;j<y;j++){
            int var=j-array[i-1];
            if(i==0) arr[i][j]=0;
            else if(j==0)   arr[i][j]=1;
            else if(var>=0){
                arr[i][j]=arr[i-1][j]+arr[i][var];
            }
            else{
                arr[i][j]=arr[i-1][j];
            }
        }
    }
    printf("%d",arr[x-1][y-1]);

}
