Fibonacci Sequence
An integer value N is passed as the input. The program must print the first N terms in the Fibonacci sequence.
Input Format: The first line denotes the value of N.
Output Format: The first N terms in the Fibonacci sequence (with each term separated by a space)
Boundary Conditions: 3 <= N <= 50
Example Input/Output 1:
Input:
5
Output:
0 1 1 2 3
Example Input/Output 2:
Input:
10
Output:
0 1 1 2 3 5 8 13 21 34
n=int(input())
a,b,c=0,1,0
while c<n:
    print(a,end=" ")
    t=a+b
    a=b
    b=t
    c=c+1
