Find Generation Gap
Find Generation Gap: The family hierarchy is given in N lines. Each line contains parent and child separated by a space. The program must find the number of generations present between the first and last generation.
Boundary Condition(s):
1 <= N <= 100
1 <= Length of parent, child <= 100
Input Format:
The first line contains N.
The next N lines contain the parent and child names separated by a space.
Output Format:
The first line contains the specified output.
Example Input/Output 1:
Input:
3
son grandson
father son
grandfather father
Output:
2
Explanation;
The first generation member is grandfather.
The last generation member is grandson.
There are two generations between them (father and son) hence the output is 2.
Example Input/Output 2:
Input:
6
grandfather father
father son1
father son2
son1 grandson1
grandson1 greatgrandson1
grandson1 greatgrandson2
Output:
3
Explanation:
The first generation member is grandfather.
The last generation members are greatgrandson1 and greatgrandson2.
There are three generations between them (father, son1 and grandson1) hence the output is 3.
q=[]
def find(a,d,c):
    if a not in d:
        q.append(c)
    else:
        for i in d[a]:
            find(i,d,c+1)
a=int(input())
d={}
l,r=[],[]
for i in range(a):
    k=input().split()
    l.append(k[0])
    r.append(k[1])
    if k[0] not in d:
        d[k[0]]=[]
    d[k[0]].append(k[1])
for i in l:
    if i not in r:
        a=i 
        break
find(a,d,0)
print(max(q)-1)
