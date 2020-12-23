Non Common Alphabets
Non Common Alphabets: Two strings S1 and S2 are passed as input. The program must print the non-common alphabets in the strings S1 and S2. Assume the alphabets in S1 and S2 will be in lower case.
Note: Print the non-common alphabets in S2 first and then print the non-common alphabets in S1.
Boundary Condition(s):
Length of S1 and S2 will be from 3 to 100.
Input Format:
The first line contains the value of string S1 
The second line contains the value of string S2 
Output Format:
The first line contains the non-common alphabets.
Example Input/Output 1:
Input:
apple
mango
Output:
mngople
Example Input/Output 2:
Input:
delicacy
celibacy
Output:
bd
Python:
a=input().strip();b=input().strip()
l,m,o=[],[],[]
for i in a:
   if i not in l:
      l.append(i)
for i in b:
   if i not in m:
      m.append(i)
for i in m:
   if i not in l:
      o.append(i)
for i in l:
   if i not in m:
      o.append(i)
print(*o,sep='')
s1=input().strip()
s2=input().strip()
l=[0]*128
l1=[0]*128 
for i in s1:
    l[ord(i)]=1
for i in s2:
    l1[ord(i)]=1
for i in s2:
    if(l[ord(i)])!=1:
        print(i,end='')
for i in s1:
    if(l1[ord(i)])!=1 and l[ord(i)]==1:
        l[ord(i)]=0
        print(i,end='')
