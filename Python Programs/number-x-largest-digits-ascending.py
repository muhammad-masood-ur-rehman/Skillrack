Number - X Largest Digits Ascending
Number - X Largest Digits Ascending: Accept a number N and print the first X largest digits in N in ascending order.
Input Format:
The first line contains N and X separated by a space.
Output Format:
The first line contains the X largest digits in N in ascending order.
Boundary Conditions:
1 <= N <= 999999999999999
1 <= X <= 10
Example Input/Output 1:
Input:
1684285215
3
Output:
568
Example Input/Output 2:
Input:
90217623
2
Output:
79
n=input().strip()
m=int(input())
l=[]
t=list(sorted(set(n)))
for i in range(m):
    l.append(t[::-1][i])
print(*l[::-1],sep="")
