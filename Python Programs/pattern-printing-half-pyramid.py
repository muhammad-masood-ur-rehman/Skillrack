Pattern Printing-Half Pyramid
The number of rows N is passed as the input. The program must print the half pyramid using asterisk *.
Input Format:
The first line contains N.
Output Format:
N lines representing the half pyramid pattern using * (A single space is used to separate the *).
Boundary Conditions:
2 <= N <= 100
Example Input/Output 1:
Input:
5
Output:
*
* *
* * *
* * * *
* * * * *
Example Input/Output 2:
Input:
3
Output:
*
* *
* * *
n=int(input())
for i in range(n):
    for j in range(0,i+1):
        print("* ",end="")
