Length of Line
A line is denoted by the x and y co-ordinates of the two end points. The program must print the length of the line.
Input Format:
First line will contain the x and y co-cordinates of point 1 separated by a space.
Second line will contain the x and y co-cordinates of point 2 separated by a space
Output Format:
The length of the line rounded up to two decimal places. If there is no floating point representation then a .00 is to appear at the end of the output.
Sample Input/Output:
Example 1:
Input:
0 4
3 0
Output:
5.00
Example 2:
Input:
2 2
14 7
Output:
13.00
Example 3:
Input:
0 0
3 3
Output:
4.24
import math
x,y=input().split(),input().split()
x,y=[int(i) for i in x],[int(i) for i in y]
t,t1=abs(x[0]-y[0]),abs(x[1]-y[1])

print("%.2f" %math.sqrt(t*t+t1*t1))
