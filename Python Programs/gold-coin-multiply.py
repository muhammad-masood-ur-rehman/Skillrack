Gold Coin Multiply
A gold pot has the ability to multiply the count of gold coins in it every day. Every day the count of gold coin grows X times. Given initial count of gold coins, the value of X and number of days D, the program must print the count of gold coins at the end of D days.
Boundary Condition(s):
1 <= X, D, coin count <= 1000
Input Format:
The first line contains coin count, X and D values separated by space(s).
Output Format:
The first line contains the count of coin at the end of D days.
Example Input/Output 1:
Input:
10 3 2
Output:
90
Example Input/Output 2:
Input:
20 4 6
Output:
81920
c,x,d=[int(i) for i in input().split()]
c,x,d=int(c),int(x),int(d)
while(d>0):
    c*=x;
    d-=1;
print(int(c))
