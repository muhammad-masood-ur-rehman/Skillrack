Sum of Prime Numbers
Given an integer matrix of size M*N as input, the program must print the sum of prime numbers present in the given matrix.
Boundary Condition(s):
1 <= M, N <= 50
Input Format:
The first line contains the values of M and N separated by a space.
The next M lines contain N elements each separated by space(s).
Output Format:
The first line contains the sum of prime numbers present in the matrix.
Example Input/Output 1:
Input:
3 4
1 2 3 4
5 6 7 8
9 10 11 12
Output:
28
Explanation :
The prime numbers are 2, 3, 5, 7, 11 and their sum is 28.
Example Input/Output 2:
Input:
3 3
3 4 2
1 2 6
5 4 1
Output:
12
Explanation :
The prime numbers are 3, 2, 2, 5 and their sum is 12.
def prime(s):
    if s==1:
        return 0
    for i in range(2,s):
        if s%i==0:break
    else: return 1 
a,b=map(int,input().split());k=[]
l=[list(map(int,input().split())) for i in range(a)]
for i in range(a):
    for j in range(b):
        if prime(l[i][j]):
            k.append(l[i][j])
print(sum(k))
