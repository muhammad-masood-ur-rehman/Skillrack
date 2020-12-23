Difference between a number and it's reverse
The number N is passed as input. The program must print the difference between the number N and it's reverse R.
Input Format:
The first line denotes the value of N.
Output Format:
The first line contains the value of N-R
Boundary Conditions:
10 <= N <= 9999999
Example Input/Output 1:
Input:
42
Output:
18
Explanation:
The output is 42-24 = 18
Example Input/Output 2:
Input:
555
Output:
0
Explanation:
The output is 555-555 = 0
Example Input/Output 3:
Input:
125
Output:
-396
Explanation:
The output is 125-521 = -396
a=input().strip()
print(int(a)-int(a[::-1]))
