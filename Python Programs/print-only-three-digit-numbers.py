Print - Only Three Digit Numbers
The program must accept a string S and print only the three digit numbers in it (in the order of occurrence). The most significant digits can also be one or more 0's. If there are no three digit numbers in the string, then print -1 as the output.
Hint: Try using Regular Expressions to solve
Input Format:
The first line will contain S.
Output Format:
The first line will contain the three digit numbers separated by a space.
Boundary Conditions:
1 <= Length of S <= 99999
Example Input/Output 1:
Input:
abc55def789KK23GOOD9999910ONEM109ORE19k6
Output:
789 109
Example Input/Output 2:
Input:
ABCDEF
Output:
-1
Example Input/Output 3:
Input:
qYPxm004xktD000Mq9y026lH8pBDz
Output:
004 000 026
z=input().strip();o='';k=[];p=[]
for i in z:
    if i.isdigit():o+=i
    else:
        if len(o)!=0:k.append(o);o=''
if len(o)!=0:k.append(o)
if len(k)==0:print(-1);exit()
else:
    for i in k:
        if len(i)==3:p.append(i)
if len(p)!=0:
    for i in p:print(i,end=' ')
else:print(-1)
