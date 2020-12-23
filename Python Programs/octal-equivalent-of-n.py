Octal Equivalent Of N
Octal Equivalent Of N: Given an integer N as input, the program must print the octal equivalent of N.
Boundary Condition(s):
1 <= N <= 10000000
Input Format:
The first line contains the value of N.
Output Format:
The first line contains the octal equivalent of N.
Example Input/Output 1:
Input:
4756
Output:
11224
Explanation:
The octal equivalent of 4756 is 11224.
Example Input/Output 2:
Input:
49467
Output:
140473
Explanation:
The octal equivalent of 49467 is 140473.
def decimal_to_octal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10;

    return octal;

decimal = int(input())
print(decimal_to_octal(decimal))
