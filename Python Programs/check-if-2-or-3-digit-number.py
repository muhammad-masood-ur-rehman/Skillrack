Check if 2 or 3 Digit Number
Check if 2 or 3 Digit Number: Given an integer N as input, the program must print YES if the given integer N is a two digit or a three digit number. Else the program must print NO.
Boundary Condition(s):
1 <= N <= 99999999
Input Format:
The first line contains the value of N.
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input:
245
Output:
YES
Example Input/Output 2:
Input:
23847
Output:
NO
n=input();k=len(n)
print('YES') if k==2 or k==3 else print('NO') 
