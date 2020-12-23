Only Fibonacci
N integers are passed as input. The program must print only the integers that are present in the Fibonacci series.
Input Format: The first line contains N. The second line contains N integers separated by a space.
Output Format: Integers that are part of the Fibonacci series in their order of occurrence (separated by a space).
Boundary Conditions: 1 <= N <= 9999999
Example Input/Output 1:
Input:
5
13 2 10 4 8
Output:
13 2 8
Explanation: The Fibonacci series is 0 1 1 2 3 5 8 13 21 and so on. So the input values that are part of the Fibonacci series are 13 2 8 in their order of occurrence.
n,n1=int(input()),1000
l,l1=[int(i) for i in input().split()],[]
a,b,c,t=0,1,0,0
while c<n1:
    l1.append(a)
    t=a+b
    a,b=b,t
    c+=1
print(*[x for x in l if x in l1])
