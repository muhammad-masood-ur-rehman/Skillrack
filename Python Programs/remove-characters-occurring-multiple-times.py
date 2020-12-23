Remove characters occurring multiple times
A string S is passed as the input. The program must remove all characters which appear more than once. If all the characters in a string are occurring more than once, then print -1 as output.
Input Format: The first line contains the value of S.
Boundary Conditions: 2 <= Length of S <= 100
Output Format: The string with the characters occurring more than once removed.
Example Input/Output 1:
Input:
level
Output:
v
Explanation: l and e occur more than once. Hence they are removed.
Example Input/Output 2:
Input:
mistake
Output:
mistake
Example Input/Output 3:
Input:
ababab
Output:
-1
s=input()
l=[a for a in s if s.count(a)==1]
l=''.join(str(i) for i in l)
if len(l)==0:
    print("-1")
else:
    print(l)
