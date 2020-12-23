Right Angle Triangle
Right Angle Triangle: The length of the three sides of a triangle A, B and C are passed as the input. The program must check it it's a right angled triangle. Print YES or NO based on the check.
Input Format:
The first line contains A.
The second line contains B.
The third line contains C.
Output Format:
The first line contains YES or NO
Boundary Conditions:
1 <= A, B, C <= 9999
Example Input/Output 1:
Input:
5
3
4
Output:
YES
Example Input/Output 2:
Input:
11
6
9
Output:
NO
a,b,c=int(input()),int(input()),int(input())
a,b,c=sorted([a,b,c])
r=abs(a**2+b**2-c**2)
if r<0.1:
    print("YES")
else:

    print("NO")
