Print Digits - X and Y
The program must accept two integers X and Y as the input. The program must print all the digits from the unit digit of X to the unit digit of Y as the output.
Example Input/Output 1:
Input:
512 69
Output:
2 3 4 5 6 7 8 9
Example Input/Output 2:
Input:
37 44
Output:
7 6 5 4
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int X, Y, unitDigitX, unitDigitY;
    scanf("%d %d", &X, &Y);
    unitDigitX = X%10;
    unitDigitY = Y%10;
    if(unitDigitX>unitDigitY)
    {
        for(int digit = unitDigitX; digit >= unitDigitY; digit--)
        {
            printf("%d ", digit);
        }
    }
    else
    {
        for(int digit = unitDigitX; digit <= unitDigitY; digit++)
        {
            printf("%d ", digit);
        }
    }
    return 0;
}
