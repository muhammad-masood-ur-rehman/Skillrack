Swap Two Numbers
The program must accept two integers X and Y as the input. The program must swap and print those two integers as the output. Please fill in the blanks of code so that the program runs successfully.
Example Input/Output 1:
Input:
3 8
Output:
8 3
Example Input/Output 2:
Input:
7 10
Output:
10 7
X, Y = [int(val) for val in input().split()]
X = X ^ Y
Y = X ^ Y
X = X ^ Y
print(X, Y)
X, Y = [int(val) for val in input().split()]
X,Y=Y,X
print(X, Y)
X, Y = [int(val) for val in input().split()]
temp = X
X = Y
Y = X
print(X, Y)
