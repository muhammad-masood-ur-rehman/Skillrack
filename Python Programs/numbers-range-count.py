Numbers - Range Count
Given N distinct integers, the program must print the number of ranges R present. A range is defined as two or more consecutive integers.
Input Format:
The first line contains N. The second line contains N integer values separated by a space.
Output Format:
The first line contains R.
Boundary Conditions:
2 <= N <= 100000
1 <= R <= 10000
Example Input/Output 1:
Input:
5 2 1 4 9 3
Output:
1
Explanation:
The only range which is present is 1 2 3 4.
9 is not a range (as a range needs two or more consecutive integers).
Example Input/Output 2:
Input:
7 1 3 11 -15 -20 9 5
Output:
0
n=int(input())
a=[int(i)for i in input().split()]
a.sort()
c=1;b=[]
for i in range(len(a)-1):
    if a[i]+1==a[i+1]:
        c+=1
    else:
        b.append(c)
        c=1
b.append(c)

print(sum(i>1 for i in b))
