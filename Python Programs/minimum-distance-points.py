Minimum distance points
Given 'n' points in an X-Y plane , write an algorithm and the subsequent Python code to determine the pair of points that are closer. Distance between two points (x1, y1) and (x2, y2) is determined using the formula.

Consider only two decimal places of distance for comparison. When there are multiple points with the same minimum distance print all points
Input Format
Number of points
x coordinate of point1
y coordinate of point1
x coordinate of point2
y coordinate of point2
...
Output format
Point1 and Point2 that have minimum distance between them
import math
dist = lambda a,b,x,y : format(math.sqrt((a-b)**2+(x-y)**2), '.2f')
n = int(input())
x,y,mixx,l,sl=0,0,0,[],[]
for i in range(n):
    x = int(input())
    y = int(input())
    l.append((x,y))
for i in range(n-1):
    x,y = l[i][0],l[i][1]
    for j in range(i+1,n):
        a,b = l[j][0],l[j][1]
        d = float(dist(x,a,y,b))
        if i == 0 and j == 1:
            mixx = d
        if d < mixx:
            sl = []
            sl.append((x,y))
            sl.append((a,b))
            mixx = d
        elif d == mixx:
            sl.append((x,y))
            sl.append((a,b))
            mixx = d
for i in sl:
    print(i)
