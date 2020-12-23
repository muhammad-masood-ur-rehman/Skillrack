C - Stack - Reverse Integers
An array of N integers is given as input. The program must reverse the integers using a stack. Fill in the missing lines of code to implement the functions push and pop so that the program runs successfully.
Boundary Condition(s):
1 <= N <= 1000
Input Format:
The first line contains the value of N.
The second line contains N integers separated by space(s).
Output Format:
The first line contains N integers separated by a space.
Example Input/Output 1:
Input:
4
10 20 30 40
Output:
40 30 20 10
Example Input/Output 2:
Input:
5
73 92 80 18 73
Output:
73 18 80 92 73
#include <stdio.h>
int stack[1000];
int top=-1;
void push(int val){
    stack[++top]=val;
    return;
}
int pop(){
    return stack[top--];
}
int main()
{
    int N, value, ctr;
    scanf("%d", &N);
    for(ctr=0; ctr<=N-1; ctr++)
    {
        scanf("%d", &value);
        push(value);
    }
    while(top != -1){
        printf("%d ",pop());
    }
    return 0;
}
