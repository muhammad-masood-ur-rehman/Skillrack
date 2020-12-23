First M multiples of N
The number N is passed as input. The program must print the first M multiples of the number
Input Format:
The first line denotes the value of N.
The second line denotes the value of M.
Output Format:
The first line contains the M multiples of N separated by a space.
Boundary Conditions:
1 <= N <= 999999
Example Input/Output 1:
Input:
5
7
Output:
5 10 15 20 25 30 35
Example Input/Output 2:
Input:
50
11
Output:
50 100 150 200 250 300 350 400 450 500 550
a=int(input())
b=int(input())
for i in range(1,b+1):
    print(a*i,end=" ")
