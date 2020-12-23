Print Odd or Even
The program must accept an integer N as the input. The program must print Odd if N is odd. Else the program must print Even as the output. Please fill in the blanks of code so that the program runs successfully.
Boundary Condition(s):
1 <= N <= 10^5
Example input/Output 1:
Input:
16
Output:
Even
Example input/Output 2:
Input:
7
Output:
Odd
N = int(input())
if N & 1:
    print("Odd")
else:
    print("Even")
