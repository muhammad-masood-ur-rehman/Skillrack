Double Array Values
Given N integers, the program must double the values and print them.
Input Format:
First line contains N
Second line contains N integers separated by a space.
Output Format:
First line contains N integer values which are twice the input array values separated by a space.
Boundary Conditions:
2 <= N < = 99999
Example Input/Output 1:
Input:
5
100 200 300 44 500
Output:
200 400 600 88 1000
n=int(input())
li=list(map(int,input().split()))
temp1=[]
for i in li:
    n=i*2
    temp1.append(n)
print(*temp1)
    
