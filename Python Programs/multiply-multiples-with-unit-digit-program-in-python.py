Multiply Multiples with Unit Digit Program In Python
Multiply Multiples with Unit Digit: Two numbers X and Y are passed as the input where Y > X. Another number N is also passed as the input to the program. The program must print the values which are nothing but multiples of N from Y to X (in the reverse order inclusive of Y and X) multiplied with their unit digit.
Boundary Condition(s):
2 <= Y <= 1000000
X < Y
1 <= N <= 100
Input Format:
The first line contains the value of X and Y separated by a space.
The second line contains the value of N.
Output Format:
The first line contains the numerical values as mentioned in the problem statement.
Example Input/Output 1:
Input:
5 25
3
Output:
96 21 144 75 24 81 36
Explanation:
The numbers from 25 to 5 divisible by 3 are 24 21 18 15 12 9 6.
Their unit digits are 4 1 8 5 2 9 and 6 respectively.
So the numbers are 24*4=96, 21*1 = 21, 18*8 = 144, 15*5 = 75, 12*2=24, 9*9 = 81 and 6*6 = 36.
a,b=map(int,input().split())
c=int(input())
k=[i for i in range(b,a-1,-1) if i%c==0]
l=[i%10 for i in k]
for i in range(len(k)):
    print(*[k[i]*l[i]],end=" ")
