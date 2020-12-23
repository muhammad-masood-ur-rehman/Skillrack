Decimal Equivalent of Last X Bits using Bitwise Operators
The program must accept two integers N and X as the input. The program must print the decimal equivalent of last X bits in N as the output.
Boundary Condition(s):
1 <= N <= 10^5
1 <= X <= 17
Input Format:
The first line contains two integers N and X separated by a space.
Output Format:
The first line contains an integer as per the given condition.
Example Input/Output 1:
Input:
23 3
Output:
7
Explanation:
The binary representation of 23 is 10111.
The last 3 bits of 23 is 111.
The decimal value of 111 is 7, so 7 is printed as the output.
Example Input/Output 2:
Input:
45 5
Output:
13
N, X = [int(val) for val in input().split()]
print(N & ((1 << X) -1))
