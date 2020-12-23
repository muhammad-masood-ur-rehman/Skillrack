Right Triangle Characters Pattern Program in Python
Right Triangle Characters Pattern: A string S is passed as the input to the program. The program must print the characters in the string in the pattern as mentioned in the Example Input/Output section.
Boundary Condition(s):
1 <= Length of String S <= 1000
Input Format:
The first line contains the value of S
Output Format:
Lines containing the characters in the string in the pattern as mentioned in the Example Input/Output section.
Example Input/Output 1:
Input:
machine
Output:
m
ac
hin
e***
Example Input/Output 2:
Input:
environmental
Output:
e
nv
iro
nmen
tal**
Example Input/Output 3:
Input:
caught
Output:
c
au
ght
s=input().strip()
k=0
if len(s)==1:
    print(s)
    exit()
for i in range(1,len(s)):
    if k<len(s):
        for j in range(i):
            if k<len(s):
                print(s[k],end="")
                k+=1 
            else:
                print("*",end="")
        print()
