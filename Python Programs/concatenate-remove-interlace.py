Concatenate Remove & Interlace
Concatenate Remove & Interlace: The program must accept two string values (S1 and S2) and a character CH (The character can be +, - or *) as the input. The program must print the output based on the following conditions. 
- If CH is +, the program must concatenate the string values S1 and S2. Then the program must print the concatenated string as the output. 
- If CH is -, the program must remove the characters of S2 In S1 (from left to right) and print the modified string S1. 
If all characters are removed in S1, then the program must print -1 as the output. 
- If CH is *, the program must print the characters in the string S1 interlaced with the characters in the string S2 (i.e., 1st character of S1, 1st character of S2, 2nd character of S1, 2nd character of S2, … and so on). 
Example Input/Output 1: 
Input: 
#ProGramming# 
mango#
-
Output: 
PrGrmi#
Example Input/Output 2: 
Input: 
Skill
Rack
+
Output: 
SkillRack

Example Input/Output 3:
Input:
C@rtOOn 
Spider10
*
Output: 
C5@pritdOeOrn10
s=input().strip()
d=input().strip()
c=input().strip()
if c=='+':
    print(s+d)
elif c=='-':
    for i in range(len(d)):
        for j in range(len(s)):
            if d[i]==s[j]:
                s=s.replace(s[j],'',1)
                break
    if len(s)==0:
        print(-1)
    else:
        print(s)
elif c=='*':
    for i in range(max(len(s),len(d))):
        if i<len(s):
            print(s[i],end='')
        if i<len(d):
            print(d[i],end='')
