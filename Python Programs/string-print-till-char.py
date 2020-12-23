String - Print till char
A string S is passed as input along with a character C. The program must print the string value S till C is reached.
Input Format:
The first line contains the value of S
The second line contains the value of C
Output Format:
The first line contains the value of S till C occurs.
Boundary Conditions:
2 <= Length of S <= 50
Example Input/Output 1:
Input:
environment
m
Output:
environm

Example Input/Output 2:
Input:
virus
v
Output:
v

Example Input/Output 3:
Input:
carriage
r
Output:
car
a=input().strip();b=a.index(input().strip())
print(a[:b+1])
