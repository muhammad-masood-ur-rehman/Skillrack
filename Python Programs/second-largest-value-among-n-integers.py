Second Largest Value among N integers
The program must accept N integers and print the second largest value among the N integers.
Input Format:
The first line denotes the value of N.
Next N lines will contain the N integer values.
Output Format:
The first line contains the second largest integer.
Boundary Conditions:
2 <= N <= 100
The value of the integers will be from -999999 to 999999.
Example Input/Output 1:
Input:
3
100
2200
345
Output:
345
Example Input/Output 2:
Input:
6
-23
-256
-87
-90
-11019
-2
Output:
-23
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
l.sort()
print(l[-2])
