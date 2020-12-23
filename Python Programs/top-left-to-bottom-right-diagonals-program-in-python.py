Top-left to Bottom-Right Diagonals Program In Python
The program must accept an integer matrix of size RxC as the input. The program must print the integers in the top-left to bottom-right diagonals from the top-right corner of the matrix.
Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix element value <= 1000
Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
Output Format:
The first (R+C)-1 lines, each contains the integer value(s) separated by a space.
Example Input/Output 1:
Input:
3 3
9 4 5
9 5 3
7 7 5
Output:
5
4 3
9 5 5
9 7
7
Explanation:
In the given 3x3 matrix, the integers in the top-left to bottom-right diagonals from the top-right corner of the matrix are given below.
5
4 3
9 5 5
9 7
7
Example Input/Output 2:
Input:
7 5
17 88 27 71 57
28 96 59 99 56
52 69 80 86 57
85 56 48 59 47
61 85 58 86 36
63 23 14 70 60
28 50 17 24 13
Output:
57
71 56
27 99 57
88 59 86 47
17 96 80 59 36
28 69 48 86 60
52 56 58 70 13
85 85 14 24
61 23 17
63 50
28
r,c=map(int,input().split())
m=[list(map(int,input().split())) for row in range(r)]
for i in range(1-c,r):
    for row in range(r):
        for col in range(c):
            if row-col==i:
                print(m[row][col],end=" ")
    print()   
