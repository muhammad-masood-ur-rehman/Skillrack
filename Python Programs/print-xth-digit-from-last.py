Print Xth Digit from Last
Two integers N and X are given as input. The program must print the Xth digit of N from last.
Boundary Condition(s):
1 <= N <= 999999999
1 <= X <= 9
Input Format:
The first line contains N and X separated by space(s).
Output Format:
The first line contains the Xth digit of N from last.
Example Input/Output 1:
Input:
739204 3
Output:
2
Example Input/Output 2:
Input:
90343 5
Output:
9
a,b=[int(i) for i in input().split()]
a,b=int(a),int(b)
while(b>1):
    a/=10
    b-=1
print(int(a%10))
