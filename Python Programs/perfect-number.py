Perfect Number
Given a positive integer N as the input, the program must print yes if N is a perfect number. Else no must be printed.
Input Format: The first line contains N.
Output Format: The first line contains yes or no
Boundary Conditions: 1 <= N <= 999999
Example Input/Output 1:
Input: 6
Output:
yes
Example Input/Output 2:
Input: 8
Output:
no
n=int(input())
l=[i for i in range(1,n) if n%i==0]
if n==sum(l):
    print("yes")
else:
    print("no")
