Largest & Smallest Digits Difference
A number N is passed as the input. The program must print the difference between the largest and the smallest digits in the number.
Input Format:
The first line will contain the number N.
Boundary Conditions:
10 <= N <= 99999999
Output Format:
The difference between the largest and the smallest digits in the number N.

Example Input/Output 1:
Input:
2501
Output:
5
Explanation:
The largest digit is 5. The smallest digit is 0. The difference is 5-0 = 5 is printed as the output.

Example Input/Output 2:
Input:
22
Output:
0
Explanation:
Both the largest and the smallest digit is 2. Hence the difference 2-2 = 0 is printed as the output.
s=list(input())
m=max(s);k=min(s)
print(int(m)-int(k))
