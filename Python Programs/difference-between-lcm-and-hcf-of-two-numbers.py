Difference between LCM and HCF of two numbers
Two whole numbers N1 and N2 are passed as input. The program must print the difference between the LCM and HCF of these two numbers.
Input Format:
First line will contain the value of the first number N1
Second line will contain the value of the second number N2
Output Format:
First line will contain the difference between the LCM and HCF of N1 and N2
Boundary Conditions:
1 <= N1 <= 99999
1 <= N2 <= 99999
Sample Input/Output:
Example 1:
Input:
30
45
Output:
75
Explanation:
LCM is 90 and HCF is 15. Difference = 90-15 = 75
Example 2:
Input:
100
120
Output:
580
Explanation:
LCM is 600 and HCF is 20. Difference = 600-20 = 580
from fractions import gcd
x,y=int(input()),int(input())
t=gcd(x,y)
l=x*y//t
print(l-t)
