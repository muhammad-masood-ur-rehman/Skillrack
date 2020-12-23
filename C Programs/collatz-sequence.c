Collatz Sequence
number N is passed as the input. The program must print the number of steps required for the program to reach Collatz sequence (that is reach 1).
Collatz Sequence: Suppose we select some initial number N and then build the sequence of values by the following rules:
if N is even then Nnext = N / 2 else Nnext = 3 * N + 1
For example, with N = 15 we have sequence: 15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1
After the sequence reaches 1 it enters the loop 1 4 2 1 4 2 1 and so on ….
The program must print how many steps are necessary to come to 1.
Input Format: The first line contains the value of N.
Output Format: The first line contains the number of steps required for term in the series to reach 1 (ie Collatz Sequence)
Boundary Conditions: 3 <= N <= 9999999
Example Input/Output 1:
Input:
5
Output:
5
Explanation: The series is 5 16 8 4 2 1
#include<stdio.h>
int main()
{
int n,c=0;
scanf("%d",&n);
while(n!=1)
{
    if(n%2!=0)
        n=3*n+1;
    else
        n/=2;
    c++;
}
printf("%d",c);

}
