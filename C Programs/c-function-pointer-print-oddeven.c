C - Function Pointer - Print OddEven
Three integers A, B and C are passed as input. If A is 0 the program must print the odd numbers from B to C. If A is 1 the program must print the even numbers from B to C. The function printOdd is implemented to print the odd numbers in the given range. Fill in the missing lines of code to implement the functions printEven and dispatcher to run the program successfully.
Boundary Condition(s):
1 <= B, C <= 1000000
0 <= A <= 1
Input Format:
The first line contains the value of A, B and C separated by space(s).
Output Format:
The first line contains the integers separated by a space.
Example Input/Output 1:
Input:
1 2 10
Output:
2 4 6 8 10
Example Input/Output 2:
Input:
0 1 10
Output:
1 3 5 7 9
#include<stdio.h>
void printOdd(int start, int end)
{
    start = start%2!=0? start:start+1;
    while(start <= end)
    {
        printf("%d ", start);
        start += 2;
    }
}
void printEven(int start,int end){
    while(start<=end){
        if(start%2==0) printf("%d ",start);
        start+=1;
    }
}
void dispatcher(void(*funcPtr)(),int start,int end){
    funcPtr(start,end);
}
int main()
{
    int even, start, end;
    scanf("%d %d %d",&even, &start, &end);
    void (*funcPtr)(int,int) = even == 1? printEven : printOdd;
    dispatcher(funcPtr, start, end);
    return 0;
}
