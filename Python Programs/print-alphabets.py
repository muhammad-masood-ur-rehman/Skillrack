Print Alphabets
Given two alphabets C1 and C2 as input, the program must print the alphabets from C1 to C2 (inclusive of C1 and C2).
Boundary Condition(s):
a <= C1 < z
C1 < C2 <= z
Input Format:
The first line contains the two alphabets C1 and C2 separated by space(s).
Output Format:
The first line contains the alphabets from C1 to C2 (inclusive of C1 and C2) seperated by a space.
Example Input/Output1:
Input:
a d
Output:
a b c d
Example Input/Output2:
Input:
g l
Output:
g h i j k l
a,b=map(str,input().split())
for i in range(ord(a),ord(b)+1):
    print(chr(i),end=" ")
