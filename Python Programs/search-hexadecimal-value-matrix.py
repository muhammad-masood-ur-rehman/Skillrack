Search Hexadecimal Value - Matrix
The program must accept a character matrix of size RxC containing only hexadecimal digits and an integer X as the input. The program must print YES if the hexadecimal value of X is present horizontally (left to right) in the matrix. Else the program must print NO as the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= X <= 10^18
Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by space.
The (R+2)nd line contains X.
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input:
4 5
F 3 E B 2
A 1 5 F 9
7 A 2 4 8
5 2 D D 6
45
Output:
YES
Explanation:
The hexadecimal value of 45 is 2D.
In the given 4x5 matrix, the hexadecimal value of 45 is present horizontally in the 4th row of the matrix.
F 3 E B 2
A 1 5 F 9
7 A 2 4 8
5 2 D D 6
So YES is printed as the output.
Example Input/Output 2:
Input:
3 2
3 a
5 9
a 9
89
Output:
YES
Example Input/Output 3:
Input:
5 7
5 7 7 4 d 9 5
a 8 a D 6 D C
a D 0 B 3 d 1
5 c A 7 f 1 7
3 a a 3 D 8 C
90
Output:
NO
a,b=map(int,input().split())
l=["".join(input().split()).upper() for i in range(a)]
c=int(input())
h=hex(c)[2:].upper()
for i in l:
    if h in i:
        print("YES")
        break
else:
    print("NO")
