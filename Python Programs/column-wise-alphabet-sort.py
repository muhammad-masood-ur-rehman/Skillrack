Column-wise Alphabet Sort
A matrix of size N*N is passed as input. The program must sort the matrix(lexicographically) column-wise and prints the matrix.
Boundary Condition:
1 <= N <= 100
Input Format:
The first line contains the value of N.
The Next N lines contain N characters each separated by one space.
Output Format:
The first N lines contain the sorted matrix with each value separated by one space.
Example Input/Output1:
Input:
3
i u q
p o a
p c r
Output:
i c a
p o q
p u r
Explanation:
The first column is sorted as i p p.
The second column is sorted as c o u.
The third column is sorted as a q r.
Example Input/Output2:
Input:
7
j l a o i d y
h k i y a j l
l k h b n k a
u y z p q l p
i y f h c a z
o i a q e s c
p o u y a x f
Output:
h i a b a a a
i k a h a d c
j k f o c j f
l l h p e k l
o o i q i l p
p y u y n s y
u y z y q x z
a=int(input())
l,c=[],[]
for i in range(a):
    l.append(list(map(str,input().split())))
b=[[l[j][i] for j in range(a)] for i in range(a)]
for i in b:
    c.append(sorted(i))
l=[[c[j][i] for j in range(a)] for i in range(a)]
for i in l:
    print(*i)
