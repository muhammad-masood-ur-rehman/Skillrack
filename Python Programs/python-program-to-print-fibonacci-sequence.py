Python Program To Print Fibonacci Sequence
An integer value N is passed as the input. The program must print the first N terms in the Fibonacci sequence.
Input Format:
The first line denotes the value of N.
Output Format:
The first N terms in the Fibonacci sequence (with each term separated by a space)
Boundary Conditions:
3 <= N <= 50
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
n1,n2=0,1
count=0
while count<n:
    print(n1,end=" ")
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
