String - Repeating Alphabets
Given a string S as the input, print the distinct alphabets in S that occur more than once. The alphabets must be printed based on the order of their occurrence in S.
Input Format:
The first line contains S.
Output Format:
The first line contains the distinct alphabets in S that occur more than once.
Boundary Conditions:
2 <= LENGTH of S <= 200
Example Input/Output 1:
Input:
Apple
Output:
p
Example Input/Output 2:
Input:
environment
Output:
en
n=input().strip()
s=""
k=[]
for l in n:  
    if n.count(l)>1:
        s+=l
for i in s:
    if i not in k:
        k.append(i)
for i in k:
    print (i,end="")
