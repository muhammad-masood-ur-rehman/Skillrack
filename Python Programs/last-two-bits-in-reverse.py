Last Two Bits in Reverse
The program must accept an integer N as the input. The program must print the last two bits of N in reversed order as the output. 
Example Input/Output 1:
Input:
14
Output:
01
Example Input/Output 2:
Input:
8
Output:
00
N = int(input())
print(N & 1, end="")
print((N >> 1) & 1)
