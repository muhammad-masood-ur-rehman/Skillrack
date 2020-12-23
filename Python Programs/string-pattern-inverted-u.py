String Pattern - Inverted U
String Pattern - Inverted U: Three strings S1, S2 and S3 are passed as the input. The program must print the pattern as shown in the Example Input/Output section. Out of these three strings, the two strings that are printed along the left most column and the right most column will be of the same length. The string printed along the first row may or may not be equal in length to the other two strings but it's first character will be same as the first character of the string in the left most column and it's last character will be same as the first character of the string in the right most column. The string values appearing on the top, left, right can appear in any order in the input.
Boundary Conditions(s):
2 <= Length of strings <= 1000
Input Format:
The first line contains the string value S1.
The second line contains the string value S2.
The third line contains the string value S3.
Output Format:
The program must print the output as specified in Example Input/Output section.
Example Input/Output 1:
Input:
PANTHER
PATNA
ALLERGY
Output:
PATNA
A***L
N***L
T***E
H***R
E***G
R***Y
Example Input/Output 2:
Input:
MANGOES
ECSTASY
MIRACLE
Output:
MIRACLE
A*****C
N*****S
G*****T
O*****A
E*****S
S*****Y
a=input().strip()
b=input().strip()
c=input().strip()
if a[0]==b[0]:
    x=a
    y=b
    k=c
elif a[0]==c[0]:
    x=a
    y=c
    k=b
else:
    x=b
    y=c
    k=a
if x[-1]==k[0]:
    m=x 
else:
    m=y 
print(m)
if len(a)==len(b):
    g=a[1:]
    h=b[1:]
elif len(b)==len(c):
    g=b[1:]
    h=c[1:]
else:
    g=a[1:]
    h=c[1:]
v=0
w=0
for i in range(len(k)-1):
  l=[]
  if v<len(g):
      l.append(g[v])
      v+=1
  for j in range(len(m)-2):
      l.append('*')
  if w<len(g):
      l.append(h[w])
      w+=1
  for i in l:
      print(*i,end='')
  print()
