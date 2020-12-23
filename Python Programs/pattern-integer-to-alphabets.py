Pattern - Integer to Alphabets
Given a number N, convert the number to character values based on alphabet positions as given in Example Input/Output.
Hint: Use modulo and division operator repeatedly to obtain the pattern.
Boundary Condition(s):
1 <= N <= 10000000
Input Format:
The first line contains N.
Output Format:
The first line contains the string representation.
Example Input/Output 1:
Input:
10
Output:
J
Example Input/Output 2:
Input:
28
Output:
AB
n=int(input()) 
a="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
s="" 
if(n<=26):
    print(a[n-1],end="") 
    exit() 
while(n>26):
    s+=a[(n%26)-1] 
    n//=26 
s+=a[n-1] 
print(s[::-1])
