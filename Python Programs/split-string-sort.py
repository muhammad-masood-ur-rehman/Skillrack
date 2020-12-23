Split String & Sort
An even length string S is passed as the input. The program must split the string into two parts S1 and S2 and sort them in ascending order.
Input Format:
The first line contains S.
Output Format:
Two lines containing S1 and S2 sorted in ascending order.
Boundary Conditions:
2 <= Lenngth of S <= 10000
Example Input/Output 1:
Input:
manage
Output:
age
man
s=input().strip()
l=len(s)//2
h=s[l:]
g=s[:l]
l=[]
l.append(h)
l.append(g)
print(*l,sep="\n")
