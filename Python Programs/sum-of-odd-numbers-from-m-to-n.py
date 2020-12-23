Sum of odd numbers from M to N
Two numbers M and N are passed as the input. The program must print the sum of odd numbers from M to N (inclusive of M and N).
Input Format:
The first line denotes the value of M
The second line denotes the value of N
Output Format:
Sum of odd numbers from M to N (inclusive of M and N).
Boundary Conditions:
1 <= M <= 9999999
M < N <= 9999999
Example Input/Output 1:
Input:
2
11
Output:
35
Explanation:
The odd numbers from 2 to 11 are 3 5 7 9 11.
Their sum is 35.
Example Input/Output 2:
Input:
55
111
Output:
2407
n=int(input())
m=int(input())
t=0
for i in range(n,m+1):
    if i%2==1:
        t=t+i 
print(t)
