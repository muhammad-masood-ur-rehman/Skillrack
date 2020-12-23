Unit Digit - Ascending and Descending
The program must accept two integers as the input. The program must sort the two integers in ascending order based on their unit digit and print them as the output. If the unit digits are same then sort the two integers in descending order and print them as the output.
Example Input/Output 1:
Input:
57 102
Output:
102 57
Example Input/Output 2:
Input:
275 15
Output:
275 15
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int X, Y, unitDigitX, unitDigitY;
    scanf("%d %d",&X,&Y);
    unitDigitX = X%10;
    unitDigitY = Y%10;
    if(unitDigitX == unitDigitY)
    {
        if(X > Y)
        {
            printf("%d %d", X, Y);
        }
        else
        {
            printf("%d %d", Y, X);
        }
    }
    else
    {
        if(unitDigitX < unitDigitY)
        {
            printf("%d %d", X, Y);
        }
        else
        {
            printf("%d %d", Y, X);
        }
    }
    return 0;
}
