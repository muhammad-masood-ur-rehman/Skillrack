﻿Atleast Two Less Than L
Three integers A, B, C are passed as input to the program. Another value L is also passed as the input to the program. The program must print yes if at least  two out of the three integers A, B, C are less than L. Else the program must print no.
Boundary Condition(s):
1 <= A, B, C <= 999999
1 <= L <= 999999
Input Format:
The first line contains A, B and C separated by a space.
The second line contains L.
Output Format:
The first line contains the value yes or no
Example Input/Output 1:
Input:
200 300 400
350
Output:
yes
Explanation:
200 and 300 are less than 350. Hence the output is yes
 
Example Input/Output 2:
Input:
200 300 400
250
Output:
no
l=list(map(int,input().split()));c=0
d=int(input())
for i in l:
  if i<d:c+=1
print('yes') if c>=2 else print('no')
