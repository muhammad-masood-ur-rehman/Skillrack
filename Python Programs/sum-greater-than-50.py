Sum Greater than 50
Sum Greater than 50: Given two integers A and B as input, the program must print YES if the sum of A and B  is greater than 50. Else the program must print NO.
Boundary Condition(s):
1 <= A, B <= 999999
Input Format:
The first line contains the value of A and B separated by space(s).
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input:
25 45
Output:
YES
Example Input/Output 2:
Input:
4 2
Output:
NO
a,b=map(int,input().split())
print("YES") if a+b>50 else print("NO")
