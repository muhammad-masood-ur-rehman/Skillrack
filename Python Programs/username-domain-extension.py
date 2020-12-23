Username Domain Extension
Username Domain Extension: Given a string S which is of the format USERNAME@DOMAIN.EXTENSION, the program must print the EXTENSION, DOMAIN, USERNAME in the reverse order.
Input Format:
The first line contains S.
Output Format:
The first line contains EXTENSION.
The second line contains DOMAIN.
The third line contains USERNAME.
Boundary Condition:
1 <= Length of S <= 100
Example Input/Output 1:
Input:
abcd@gmail.com
Output:
com
gmail
abcd
s=input().split('@')
a=s[0]
s=s[1]
s=s.split('.')
b=s[0];c=s[1]
print(c,b,a,sep='\n')
