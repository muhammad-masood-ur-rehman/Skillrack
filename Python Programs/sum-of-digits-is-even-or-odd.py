Sum of Digits is Even or Odd
Sum of Digits is Even or Odd: Given an integer N as input, the program must print Yes if the sum of digits in a given number is even. Else it must print No.
Boundary Condition(s):
1 <= N <= 99999999
Input Format:
The first line contains the value of N.
Output Format:
The first line contains Yes or No.
Example Input/Output 1:
Input:
123
Output:
Yes
Explanation:
The sum of digits in a given number is 1+2+3 = 6.
Hence the output is Yes.
Example Input/Output 2:
Input:
1233
Output:
No
Explanation:
The sum of digits in  a given number is 1+2+3+3 = 9.
Hence the output is No.
n=input()
s=0
for i in n:
    s+=int(i)
print('Yes' if s%2==0 else print('No')
