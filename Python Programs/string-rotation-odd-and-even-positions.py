String Rotation Odd and Even Positions
A string S and two integers M and N are passed as input. The program must rotate the characters present in the odd positions of the string M times and rotate characters present in the even positions of the string N times.
Note: Rotation must be done in clockwise direction.
Boundary Condition(s):
2 <= Length of the string <= 1000
1 <= M, N <= 1000
Input Format:
The first line contains S, M and N separated by space(s).
Input Format:
The first line contains the rotated string.
Example Input/Output 1:
Input:
technology 2 3
Output:
logotycenh
Explanation:
The characters present in the odd positions are tcnlg. When rotated 2 positions, the value is lgtcn.
The characters present in the even positions are ehooy. When rotated 3 positions, the value is ooyeh.
Hence the rotated string value is logotycenh
Example Input/Output 2:
Input:
abcde 1 1
Output:
edabc
Explanation:
Characters in odd positions are a, c and e which are rotated once to become eac.
Characters in even positions are b and d which are rotated once to become db.
So the output is edabc.
a,b,c=map(str,input().strip().split())
b=int(b) 
c=int(c)  
e,o="",""
for i in range(len(a)):
    if(i%2==0):
        o+=a[i] 
    else:
        e+=a[i]  
i=0 
while(i<b):
    e=e[1:]+e[:1] 
    i+=1
i=0 
while(i<c): 
    o=o[1:]+o[:1] 
    i+=1  
for i in range(min(len(e),len(o))):
    print(o[i],end="")
    print(e[i],end="") 
if(len(e)>len(o)):
    print(e[len(o):])
elif(len(o)>len(e)):
    print(o[len(e):])
