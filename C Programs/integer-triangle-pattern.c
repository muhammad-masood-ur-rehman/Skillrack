Integer Triangle - Pattern
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Boundary Condition(s):
2 <= N <= 50
Example Input/Output 1:
Input:
5
Output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
Example Input/Output 2:
Input:
4
Output:
1
1 2
1 2 3
1 2 3 4
#include <stdio.h>

int main()
{
    int N, row,col;
    scanf("%d", &N);
    for (row = 1; row <= N; row++)
    {
        for (col = 1; col <= row; col++)
        {
            printf("%d ", col);
        }
        printf("\n");
    }
    return 0;
}
n=int(input())
for i in range(1,n+1): 
    for j in range(1,i+1): print(j,end=" ") 
    print()
