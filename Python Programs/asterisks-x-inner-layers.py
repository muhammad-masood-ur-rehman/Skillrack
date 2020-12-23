Asterisks - X Inner Layers
Asterisks - X Inner Layers: The program must accept a character matrix of size NxN and an integer X as the input. The program must replace all the characters present in the X inner layers of the matrix with the asterisks. Finally, the program must print the modified matrix as the output.
Boundary Condition(s):
2 <= N <= 50
1 <= X <= (N+1)/2
Input Format:
The first line contains N.
The next N lines, each contains N characters separated by a space.
The (N+2)nd line contains X.
Output Format:
The first N lines, each contains N characters separated by a space.
Example Input/Output 1:
Input:
8
b z r p h u w f
c p g b p u a j
n h f a l b i g
j k x n n y k p
k v j f u b l r
z x m a t z x j
s o c u r q d j
x n t v a g y h
2
Output:
b z r p h u w f
c p g b p u a j
n h * * * * i g
j k * * * * k p
k v * * * * l r
z x * * * * x j
s o c u r q d j
x n t v a g y h
Explanation:
Here X = 2.
In the given 8x8 matrix, the 2 inner layers are highlighted below.
b z r p h u w f
c p g b p u a j
n h f a l b i g
j k x n n y k p
k v j f u b l r
z x m a t z x j
s o c u r q d j
x n t v a g y h
After replacing the characters present in the 2 inner layers with the asterisks, the matrix becomes
b z r p h u w f
c p g b p u a j
n h * * * * i g
j k * * * * k p
k v * * * * l r
z x * * * * x j
s o c u r q d j
x n t v a g y h
Example Input/Output 2:
Input:
5
H Q G I B
W A U T W
F U O W C
U G R E W
R P K C M
1
Output:
H Q G I B
W A U T W
F U * W C
U G R E W
R P K C M
n=int(input())
mat=[input().split() for i in range(n)]
x=int(input())
a=(n//2)
a1=a-x+n%2
a2=n-a1
for r in range(a1,a2):
    for c in range(a1,a2):
        mat[r][c]="*"
for row in mat:
    print(*row)
