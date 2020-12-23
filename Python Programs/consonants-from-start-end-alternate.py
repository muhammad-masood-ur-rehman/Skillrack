Consonants from Start End Alternate
Consonants from Start End Alternate: A string S is passed as the input to the program. The program must print the consonants from the start position and the consonants from the end position alternatively. No character at the same position in the string must be printed twice.
Boundary Condition(s):
1 <= Length of String S <= 1000
Input Format:
The first line contains the value of S
Output Format:
The first line contains the consonants in S printed based on the above conditions.
Example Input/Output 1:
Input:
machine
Output:
mnch
Example Input/Output 2:
Input:
environment
Output:
ntvnrmn
n=input()
m='aeiouAEIOU'
b=''
v=0
x=0
for i in n:
    if i not in m:
        b+=i 
c=b[::-1]
for i in range(len(b)):
    if i%2==0:
        print(b[v],end='')
        v+=1 
    else:
        print(c[x],end="")
        x+=1
