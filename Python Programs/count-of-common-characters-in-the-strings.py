Count of Common Characters in the Strings
Two string values S1 and S2 are passed as input. The program must print the count of common characters in the strings S1 and S2.
Input Format: First line will contain the value of string S1 Second line will contain the value of string S2
Output Format: First line will contain the count of common characters.
Boundary Conditions: Length of S1 and S2 is from 3 to 100.
Sample Input/Output:
Example 1:
Input:
china
india
Output:
3
Explanation: The common characters are i,n,a
Example 2:
Input:
energy
every
Output:
4
Explanation: The common characters are e,e,r,y
from collections import Counter
s1,s2=input(),input()
l=Counter(s1)&Counter(s2)

print(sum(l.values()))
