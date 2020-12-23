Unit Digit from 1 to 5
Unit Digit from 1 to 5: Given an integer N as input, the program must print YES if the unit digit is from 1 to 5. Else the program must print NO.
Boundary Condition(s):
1 <= N <= 999999
Input Format:
The first line contains the value N.
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input:
12345
Output:
YES
Example Input/Output 2:
Input:
1248
Output:
NO
n=input()
k=n[-1]
print('YES') if k in '12345' else print('NO')
