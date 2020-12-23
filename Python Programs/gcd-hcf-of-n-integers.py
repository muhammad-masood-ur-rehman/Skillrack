GCD (HCF) of N Integers
Given an array of integers of size N as input, the program must print the GCD (Greatest Common Divisor) of N integers.
Boundary Condition(s):
2 <= N <= 100
Input Format:
The first line contains the value of N.
The second line contains N values separated by space(s).
Output Format:
The first line contains a value.
Example Input/Output 1:
Input:
5
4 6 2 8 16
Output:
2
Explanation:
The divisors of 4 are 1, 2, 4.
The divisors of 6 are 1, 2, 3, 6.
The divisors of 2 are 1, 2.
The divisors of 8 are 1, 2, 4, 8.
The divisors of 16 are 1, 2, 4, 8, 16.
Therefore the common divisors are 1, 2.
The greatest of these is 2.
Hence the output is 2.
Example Input/Output 2:
Input:
2
8 12
Output:
4
Explanation:
The divisors of 8 are 1, 2, 4, 8.
The divisors of 12 are 1, 2, 3, 4, 6, 12.
Therefore the common divisors are 1, 2, 4.
The greatest of these is 4.
Hence the output is 4.
from functools import reduce
from math import gcd
n=int(input())
l=[int(i) for i in input().split()]

print(reduce(gcd,l))
