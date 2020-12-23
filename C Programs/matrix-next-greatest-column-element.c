Matrix Next Greatest Column Element
Matrix Next Greatest Column Element: A matrix of size R*C is given as input. The program must print the next greatest number present below each of the numbers. The number must also be an odd number. If there is no odd element which is also greater than current element present below then print *.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains R and C separated by space(s).
The next R lines contain C elements each separated by space(s).
Output Format:
The first R lines contain C elements each separated by a space.
Example Input/Output 1:
Input:
3 3
1 2 3
4 5 6
7 8 9
Output:
7 5 9
7 * 9
* * *
Example Input/Output 2:
Input:
4 5
46 45 -4 98 -88 
77 -44 15 -56 43 
43 -27 18 13 16 
-73 -99 -78 56 15
Output:
77 * 15 * 43 
* -27 * 13 * 
* * * * * 
* * * * *
 Max Execution Time Limit: 5000 millisecs
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int r,c;
    scanf("%d%d",&r,&c);
    
    int arr[r][c];
    
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j)
        {
            scanf("%d",&arr[i][j]);
        }
    }
    int constant=-989098;
    for(int j=0;j<c;++j)
    {
        int max=constant;
        for(int i=r-1;i>=0;--i)
        {
            if(arr[i][j]%2==1 || arr[i][j]%2==-1){
                if(arr[i][j]>max){
                    max=arr[i][j];
                    arr[i][j]=constant;
                }
                else{
                    arr[i][j]=max;
                }
            }
            else{
                arr[i][j]=max>arr[i][j] ? max : constant;
            }
        }
    }
    for(int i=0;i<r;++i)
    {
        for(int j=0;j<c;++j){
            if(arr[i][j]==constant)printf("* ");
            else printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    return;
}
