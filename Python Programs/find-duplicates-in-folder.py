Find Duplicates In Folder
The directory structure of a file system is given in N lines. Each line contains the parent folder name and child file/folder name. If a folder has two files/folders with the same name then it is a duplicate. Print all the duplicate file/folders names sorted in ascending order. If there is no duplicate print -1.
Boundary Condition(s):
1 <= N <= 100
2 <= Length of file/folder name <= 100
Input Format:
The first line contains N.
The next N lines contain parent and child file/folder name separated by space.
Output Format:
Print the duplicate file/folder names sorted in ascending order. If there is no duplicate print -1.
Example Input/Output 1:
Input:
5
videos trailer.mp4
documents word.doc
documents animal.jpg
test trailer.mp4
documents word.doc
Output:
word.doc
Example Input/Output 2:
Input:
7
src style.css
videos HD.mp4
documents sheet.xls
documents animal.jpg
test animal.jpg
documents sheet.xls
src style.css
Output:
sheet.xls
style.css
a=int(input())
d={}
e=[];f=[] 
for i in range(a):
    b,c=map(str,input().split())
    e.append(b)
    f.append(c)
x=0
for i in f:
    d.setdefault(i,[]).append(e[x])
    x+=1
ans=[]
for i in d.keys():
    s=list(set(d[i]))
    if(len(d[i])>1):
        if(len(s)!=len(d[i])):
            ans.append(i)
ans=sorted(ans)
if(ans==[]):
    print(-1)
else:
    print(*ans, sep="\n") 
d=[]
c=[]
for i in range(int(input())):
    k=input().split()
    if k not in d:
        d.append(k)
    elif k[1] not in c:
        c.append(k[1])
if not c:
    print(-1)
for i in sorted(c):
    print(i)
