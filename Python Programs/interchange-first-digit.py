Interchange First Digit
Two positive integers X and Y are passed as the input to the program. The program must interchange the first digits of X and Y and print them as the output.
Boundary Condition(s):
1 <= X, Y <= 10^7
Input Format:
The first line contains X and Y separated by a space.
Output Format:
The first line contains two integer values separated by a space.
Example Input/Output 1:
Input:
901 100
Output:
101 900
 
Explanation:
The first digit of X is 9.
The first digit of Y is 1.
So interchanging them the values are 101 and 900 which is printed as the output.
a,b=input().split()
print(b[0]+a[1:],a[0]+b[1:])
