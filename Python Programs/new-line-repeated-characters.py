New Line - Repeated Characters
The program must accept a string S as the input. The program must split the string S wherever a character occurs repeatedly(i.e., two or more occurrences). Then the program must print the substrings as the output.
Boundary Condition(s):
2 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The line(s) containing the substrings of S based on the given condition.
Example Input/Output 1:
Input:
skillrack
Output:
skil
lrac
k
Explanation:
Here S = skillrack.
The string S can be divided into three substrings as given below.
skil lrac k
The 5th character l is a repeated character.
The 9th character k is a repeated character.
Hence the output is
skil
lrac
k
Example Input/Output 2:
Input:
ENvironment
Output:
ENvironme
nt
Example Input/Output 3:
Input:
abcdabcdefge
Output:
abcd
a
b
c
defg
e
s=input().strip()
p=[];l=[]
l.append(0)
for i in range(len(s)):
    p.append(s[i])
    if p.count(s[i])>1:
      l.append(i)
for i in range(len(l)-1):
    print(s[l[i]:l[i+1]])
print(s[l[-1]:])
