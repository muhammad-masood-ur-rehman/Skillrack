Ways to climb N stairs
Ways to climb N stairs: There are N stairs to climb before reaching an office. The employees can either climb 1 stair or 2 stairs at in a single step. The program must print the count of distinct ways for an employee to climb the N stairs.
Input Format:
The first line will contain the value of N.
Output Format:
The first line will contain the number of distinct ways to climb the N stairs.
Boundary Condition(s):
1 <= N <= 99
Example Input/Output 1:
Input:
1
Output:
1
Example Input/Output 2:
Input:
2
Output:
2
Explanation:
The steps can be 1,1 or as 2
Example Input/Output 3:
Input:
5
Output:
8
Explanation:
The steps can be
1,1,1,1,1 or
1,1,1,2 or
1,2,2 or
1,1,2,1 or
1,2,1,1 or
2,2,1 or
2,1,2 or
2,1,1,1
n=int(input())
a=0
b=1
c=1
for ele in range(n-1):
    c=a+b 
    a=b
    b=c 
print(c+a)
