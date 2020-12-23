Last and First Character Words
Given a string S with spaces, the program must print only the words having it's first letter same as the last letter of the previous word. If no such word matches the specified condition print -1.
Boundary Condition(s):
1 <= Length of S1 <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the specified output.
Example Input/Output 1:
Input:
word dove think yellow wood
Output:
dove wood
Example Input/Output 2:
Input:
mint hen bob jack
Output:
-1
s=input().strip().split()
k=[s[i] for i in range(1,len(s)) if s[i-1][-1]==s[i][0]]
if len(k)!=0:
    print(*k)
else:
    print(-1)
