Reverse Alphabet Triangle Pattern
The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.
Boundary Condition(s):
2 <= N <= 26
Example Input/Output 1:
Input:
5
Output:
----a
---ba
--cba
-dcba
edcba
Example Input/Output 2:
Input:
4
Output:
---a
--ba
-cba
dcba
N = int(input())
alpha = ord('a')
for row in range(1, N+1):
    print('-'*(N-row), end = "")
    for col in range(1, row+1):
        print(chr(alpha), end = "")
        alpha = alpha-1
    alpha = alpha+(row+1)
    print()
