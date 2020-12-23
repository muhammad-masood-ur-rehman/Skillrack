Divide by 2 for T times using Bitwise Operators
The program must accept two integers N and T as the input. The program must divide the integer N by 2 for T times and print it as the output. Please fill in the blank of code so that the program runs successfully.
Boundary Condition(s):
2 <= N <= 10^9
1 <= T <= 30
Input Format:
The first line contains N and T separated by a space.
Output Format:
The first line contains the modified value of N based on the given condition.
Example Input/Output 1:
Input:
80 2
Output:
20
Explanation:
80/2 = 40
40/2 = 20
After dividing 80 by 2 for 2 times, the value becomes 20. So 20 is printed.
Example Input/Output 2:
Input:
63 3
Output:
7
N, T = [int(val) for val in input().split()]
print(N >> T)
