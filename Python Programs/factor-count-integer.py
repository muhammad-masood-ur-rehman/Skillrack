Factor Count - Integer
A number N is passed as input. The program should print the count of factors for the number N.
Input Format:
The first line will contain the number N.
Output Format:
The first line will contain the count of factors for the number N.
Boundary Condition(s)
1 <= N < 10^7

Example Input/Output 1:
Input:
100
Output:
9
Example Input/Output 2:
Input:
6
Output:
4
l=[];
n=int(input())
for i in range(1,n+1):
        if n%i==0:
            l.append(i)
print(len(l))
