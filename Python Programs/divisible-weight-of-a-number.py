Divisible weight of a number
A number N's divisible weight is defined as the count of numbers from A1 to Ax which divide it without leaving a remainder.
Input Format:
First line contains total number of test cases, denoted by T.
Second line will contain the value of A1 and Ax separated by a space.
Next T lines contain value of N for each test case.
Output Format:
T lines containing the weight of the number.
Boundary Conditions / Constraints:
1 <= T <= 25
1 <= A1 .. Ax <= 100
1 <= N <= 9999999
Example Input/Output 1:
Input:
3
1 9
63
108
77
Output:
4
6
2
Explanation:
4 numbers divide 63 from 1 to 9 - 1,3,7,9
6 numbers divide 108 from 1 to 9 - 1,2,3,4,6,9
2 numbers divide 77 from 1 to 9 - 1,7
n=int(input())
a,b=map(int,input().split())
for _ in range(n):
    x=int(input())
    c=0
    for i in range(a,b+1):
        if(x%i==0):
            c+=1
    print(c)
