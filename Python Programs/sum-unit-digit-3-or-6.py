Sum - Unit Digit 3 or 6
The program must accept N integers as the input. The program must print the sum of integers having the unit digit as 3 or 6 as the output. If there is no such integer then the program must print -1 as the output.
Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^5
Example Input/Output 1:
Input:
5
12 43 30 606 7337
Output:
649
Example Input/Output 2:
Input:
4
52 84 365 134
Output:
-1
N = int(input())
numList = [int(val) for val in input().split()]
sumVal, printed = 0, False
for val in numList:
    if val % 10 == 3 or val % 10 == 6:
        sumVal += val
        printed = True
print('-1' if sumVal == 0 else sumVal)
