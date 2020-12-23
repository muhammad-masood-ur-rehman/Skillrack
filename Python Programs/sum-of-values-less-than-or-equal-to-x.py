Sum of Values Less Than or Equal to X
Sum of Values Less Than or Equal to X: A set of N positive integers are passed as the input. Another number X which may or may not be present in these N integers is also passed as the input. The program must print the sum of the values (in the N integers) which are less than or equal to X).
Boundary Condition(s):
3 <= N <= 20
Input Format:
The first line contains the value of N.
The second line contains N numbers.
The third line contains the value of X.
Output Format:
The first line contains the sum of the  values.
Example Input/Output 1:
Input:
5
10 5 12 35 21
12
Output:
27
Example Input/Output 2:
9
9 18 27 36 45 54 63 72 81
90
Output:
582
n=int(input())
a=[int(i) for i in input().split()]
x=int(input())
c=0
for i in a:
    if i<=x:
        c+=i 
print(c)
