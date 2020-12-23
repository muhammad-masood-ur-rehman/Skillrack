Check for Rectangle or Square
The length L and breadth B of a rectangle is passed as input. If L is equal to B then the program must print "square". Else it must print "rectangle".
Input Format:
The first line contains the value of L
The second line contains the value of B
Output Format:
The first line contains the value which is square or rectangle
Example Input/Output 1:
Input:
45
45
Output:
square

Example Input/Output 2:
Input:
105
90
Output:
rectangle
a=int(input())
b=int(input())
if (a==b):
    print("square")
else:
    print("rectangle")
