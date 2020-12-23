Swap Two Numbers
The values for two numbers x and y will be passed as input to the program. The program must swap the two numbers and print them as output. Please fill in the missing lines of code so that the values of x and y are interchanged (swapped).
Input Format:
The first line will contain the value of x.
The second line will contain the value of y.
Example Input/Output 1:
Input:
10
200
Output:
200
10
Example Input/Output 2:
Input:
99
99
Output:
99
99
a=int(input())
b=int(input())
a,b=b,a
print(a,b,sep="\n")
