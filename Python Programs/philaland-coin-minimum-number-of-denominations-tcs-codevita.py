Philaland Coin (Minimum Number of Denominations) - TCS CodeVita
Minimum Number of Denominations TCS CodeVita solution in python
In a shop, the cost of products ranges from 1 to N (both inclusive). The program must accept the value of N and print the minimum of denominations of coins to purchase any product ranging from 1 to N as the output.
Consider the following example.
If N = 5, then we can make coins of {1, 2, 3, 4, 5} to purchase any item ranging from 1 to 5. But we can actually reduce the number of coins needed by using the following denominations {1, 2, 3}.
To purchase a product of price 1, we can use 1.
To purchase a product of price 2, we can use 2.
To purchase a product of price 3, we can use 3.
To purchase a product of price 4, we can use 1 and 3.
To purchase a product of price 5, we can use 2 and 3.
Boundary Condition(s):
1 <= T <= 100
1 <= N <= 5000
Input Format:
The first line contains an integer T denoting the number of test cases.
The next T lines, each contains an integer N denoting the maximum price of the product in the shop.
Output Format:
The first T lines, each contains an integer denoting the minimum number of denominations of coins required.
Example Input/Output 1:
Input:
2
5
10
Output:
3
4
Explanation:
For the test case 1, N = 5.
The minimum number of denominations of coins required is 3. {1, 2, 3} or {1, 2, 4}
For the test case 2, N = 10.
The minimum number of denominations of coins required is 4. {1, 2, 3, 4} or {1, 2, 3, 5}
Example Input/Output 2:
Input:
5
17
100
11
56
23
Output:
5
7
4
6
5
Minimum Number of Denominations Program in Python
Philaland Coin Program in Python
from math import log2, floor 
def mindenomination(n): 
    return log2(n) + 1
n = int(input())
for i in range(n):
    x=int(input())
    print(floor(mindenomination(x)))
