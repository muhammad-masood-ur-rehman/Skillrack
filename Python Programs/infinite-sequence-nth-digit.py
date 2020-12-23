Infinite Sequence Nth Digit
Infinite Sequence Nth Digit: The program must accept an integer value N and print the Nth digit in the integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 and so on till infinity.
Boundary Condition(s):
1 <= N <= 10^9
Input Format:
The first line contains N.
Output Format:
The first line contains one of the digits from 0 to 9.
Example Input/Output 1:
Input:
5
Output:
5
Explanation:
The 5th digit in the sequence 1234567 is 5.
Example Input/Output 2:
Input:
11
Output:
0
Explanation:
The 11th digit in the sequence 12345678910 is 0.
def funcDigit(n):
    x, y, m = 1, 1, {}
    while x <= 10:
        m[x] = y
        y = y + (10 ** x - 10 ** (x - 1)) * x
        x += 1
    for ele, foo in m.items():
        if n < foo:
            break
    ele -= 1
    y = m[ele]
    return str(10**(ele - 1)+(n-y)//ele)[(n - y) % ele]
n=int(input())
print(funcDigit(n))
