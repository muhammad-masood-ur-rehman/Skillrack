C - Function - Average
An array of N integers is given as input. The program must print the average with precision up to two decimal places. Fill in the missing lines of code to implement the function setAverage() to run the program successfully.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains the average with precision up to two decimal places.
Example Input/Output 1:
Input:
4
10 20 30 40
Output:
25.00
Example Input/Output 2:
Input:
5
7 8 12 21 10
Output:
11.60
#include <stdio.h>
int main()
{
    int N, index;
    double average = 0;
    scanf("%d", &N);
    int values[N];
    for(index=0; index<=N-1; index++)
    {
        scanf("%d", &values[index]);
    }
    setAverage(values, N, &average);
    printf("%.2f", average);
    return 0;
}
