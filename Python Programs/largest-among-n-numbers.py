Largest among N numbers
Number N is passed as the input. The program must accept N integer values and print the largest number L among these N numbers.
Input Format:
The first line denotes the value of N.
The next N lines denote the value of N numbers.
Output Format:
The first line denotes the value of L.
Boundary Conditions:
1 <= N <= 50
Example Input/Output 1:
Input:
3
100
200
40
Output:
200
Example Input/Output 2:
Input:
5
18
500
70
30
999
Output:
999
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
print(max(l))
