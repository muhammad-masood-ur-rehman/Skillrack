Python Program To Sort K length Sub-Strings
A string S of length L and an integer K is passed as the input. The program must sort and print all the unique combinations of the sub-strings which are of length K.
Boundary Condition(s):
1 <= L <= 25
K <= L
Input Format:
The first line contains S.
The second line contains K.
Output Format:
Each line contains a sub-string whose length is K.
Example Input/Output 1:
Input:
lemon
4
Output:
emon
lemn
lemo
leon
lmon
Explanation:
mone, onem are not printed as emon already has accounted for the combination of these 4 characters.
Example Input/Output 2:
Input:
apple
3
Output:
ale
ape
apl
app
ple
ppe
ppl
from itertools import combinations as c 
s=input().strip()
f=[]
d=int(input())
for i in range(0,len(s)+1):
    for j in list(c(s,i)):
        if len(j)==d and ''.join(j) not in f:
            f.append(''.join(j)) 
for i in sorted(f):
    print(i)
