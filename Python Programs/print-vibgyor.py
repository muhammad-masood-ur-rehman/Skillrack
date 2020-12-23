Print VIBGYOR
Print VIBGYOR: The program must accept a character CH (upper case) as input and print as per the following conditions.
For
V print Violet,
I print Indigo,
B print Blue,
G print Green,
Y print Yellow,
O print Orange,
R print Red,
otherwise print Invalid.
Boundary Condition(s):
A <= CH <=Z
Input Format:
The first line contains the value of CH.
Output Format:
The first line contains any one of the strings specified above.
Example Input/Output 1:
Input:
Y
Output:
Yellow
Example Input/Output 2:
Input:
E
Output:
Invalid
n=input()
print('Yellow') if n=='Y' else print('Indigo') if n=='I' else print ('Blue') if n=='B' else print('Green') if n=='G'else print ('Violet') if n=='V' else print('Orange') if n=='O'else print ('Red') if n=='R' else print('Invalid')
