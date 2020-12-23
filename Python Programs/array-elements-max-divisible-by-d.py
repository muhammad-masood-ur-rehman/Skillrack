Array Elements - Max Divisible by D
An array of N positive integers are passed as input. D which is a positive integer is also passed as the input. The program must print the largest element in the array which is divisible by D.
If none of the elements in the array is divisible by D, then print -1 as the output.
Input Format:
The first line contains the value of N.
The second line contains the N values, each separated by a space.
The third line contains the value of D.
Output Format:
The first line contains the largest element in the array which is divisible by D.
Boundary Conditions:
2 <= N <= 10000
1 <= D <= 9999
Example Input/Output 1:
Input:
6
10 20 30 40 50 60
4
Output:
60
n=int(input())
p=[]
l=list(map(int,input().split()))
d=int(input())
for i in l:
    if i%d==0:
        p.append(i)
print(max(p)) if len(p)!=0 else print(-1)
