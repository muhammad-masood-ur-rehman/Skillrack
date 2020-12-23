Balanced Parentheses Program in Python
The program must accept a series of Parentheses as a string. The program must print Valid if the parentheses are balanced. Else the program must print Invalid.
Boundary Condition(s):
1 <= Length of string <= 1000
Input Format:
The first line contains the string.
Output Format:
The first line contains Valid or Invalid.
Example Input/Output 1:
Input:
(( ))
Output:
Valid
Example Input/Output 2:
Input:
(( ( ))
Output:
Invalid
l='('
r=')'
clo={a:b for a,b in zip(r,l)}
def valid(st):
    s=[]
    for c in st:
        if c in l:
            s.append(c)
        elif c in r:
            if not s or s.pop()!=clo[c]:
                return False
    return not s 
s=input().strip()
if valid(s):
    print("Valid")
else:
    print("Invalid")
    
