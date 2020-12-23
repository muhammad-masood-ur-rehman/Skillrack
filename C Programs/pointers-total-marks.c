Pointers - Total Marks
Marks scored in three subjects M1, M2, M3 are given as input. The below program prints the total marks by invoking the function total().
Fill in the missing lines of code to run the program successfully.
Boundary Condition(s):
0 <= M1, M2, M3 <= 100
Input Format:
The first line contains the value of M1, M2 and M3 separated by space(s).
Output Format:
The first line contains total marks.
Example Input/Output 1:
Input:
40 60 80
Output:
180
Example Input/Output 2:
Input:
100 60 40
Output:
200
#include <stdio.h>
void total(int m1,int m2,int m3,int* s){
    *s=m1+m2+m3;
    return;
}
int main()
{
    int M1,M2,M3,sum;
    scanf("%d %d %d", &M1, &M2, &M3);
    total(M1, M2, M3,&sum);
    printf("%d",sum);
    return 0;
}
