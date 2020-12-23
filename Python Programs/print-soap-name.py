Print Soap Name
The following are the soap code characters for the soaps.
C or c - Cinthol
D or d - Dove
L or l - Lux
P or p - Pears
H or h - Hamam
For any other character - Lifebuoy
The program must accept the soap code character and print the output accordingly.
Input Format:
The first line contains the  soap code character.
Output Format:
The first line contains the name of the soap.
Example Input/Output 1:
Input:
c
Output:
Cinthol
 
Example Input/Output 2:
Input:
S
Output:
Lifebuoy
a=input().strip().lower()
s='Cinthol' if a=='c' \
else 'Dove' if a=='d' \
else 'Lux' if a=='l' \
else 'Pears' if a=='p' \
else 'Hamam' if a=='h' \
else 'Lifebuoy'
print(s)
