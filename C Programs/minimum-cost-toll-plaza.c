Minimum Cost - Toll Plaza Program
Minimum Cost - Toll Plaza Program: A taxi driver needs to drop his customer to a place. There are many toll plazas through which the taxi driver can cross the toll. The toll plazas charges (in rupees) are represented in an RxC matrix. Once the taxi driver crosses a toll plaza he cannot go back to the same toll. He can move only to top-left or top or top-right side of the current position. He may starts his ride from any column in the last row of the matrix and ends his ride at any column of first row in the matrix. The program must print the minimum cost (in rupees) required to drop the customer.
Boundary Condition(s):
2 <= R, C <= 100
Input Format:
The first line contains the value of R and C separated by a space.
The next R lines contain C values separated by space(s).
Output Format:
The first line contains the minimum cost (in rupees) required to drop the customer.
Example Input/Output 1:
Input:
6 5
3 1 7 4 2
2 1 3 1 1
1 2 2 1 8
2 2 1 5 3
2 1 4 4 4
5 2 7 5 1
Output:
8
Explanation:
One of the way he cross the toll plazas with minimum cost is given below
3 1 7 4 2
2 1 3 1 1
1 2 2 1 8
2 2 1 5 3
2 1 4 4 4
5 2 7 5 1
The minimum cost required to drop the customer is 2 + 1 + 2 + 1 + 1 + 1 = 8.
Hence the output is 8
Example Input/Output 2:
Input:
4 4
7 1 4 4
4 7 3 8
1 2 6 6
10 3 5 9
Output:
9
Max Execution Time Limit: 2000 millisecs
#include<stdio.h>
#include <stdlib.h>
#define min(x,y) x<y ? x : y
int main()
{
    int row,col;
    scanf("%d %d\n",&row,&col);
    int arr[row][col];
    
    for(int ele=0;ele<row;ele++)
    {
        for(int foo=0;foo<col;foo++)
        {
            scanf("%d",&arr[ele][foo]);
        }
    }
    for(int ele=row-2;ele>=0;ele--)
    {
        for(int foo=0;foo<col;foo++)
        {
            if(foo==0){
                arr[ele][foo]+=(min(arr[ele+1][foo],arr[ele+1][foo+1]));
            }
            else if(foo==col-1){
                arr[ele][foo]+=(min(arr[ele+1][foo],arr[ele+1][foo-1]));
            }
            else{
                int temp=min(arr[ele+1][foo],arr[ele+1][foo-1]);
                temp=min(temp,arr[ele+1][foo+1]);
                arr[ele][foo]+=temp;
            }
        }
    }
    int ans=arr[0][0];
    for(int ele=0;ele<col;ele++){
        if(arr[0][ele]<ans)ans=arr[0][ele];
    }
    printf("%d",ans);
    return;
}
