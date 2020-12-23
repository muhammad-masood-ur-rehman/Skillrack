All Possible Odd Integers
The program must accept an integer N as the input. The program must print the unique odd integers formed using all the digits of N in ascending order as the output.
Note: At least one odd digit is always present in the integer N.
Boundary Condition(s):
1 <= N <= 10^8
Input Format:
The first line contains N.
Output Format:
The first line contains the integer value(s) representing the unique odd integers formed using all the digits of N.
Example Input/Output 1:
Input:
147
Output:
147 417 471 741
Explanation:
Here N = 147.
The integers formed using all the digits of 147 are 147, 174, 417, 471, 714 and 741.
The odd integers are 147, 417, 471 and 741.
Hence the output is
147 417 471 741
Example Input/Output 2:
Input:
1035
Output:
135 153 315 351 513 531 1035 1053 1305 1503 3015 3051 3105 3501 5013 5031 5103 5301
Example Input/Output 3:
Input:
6772
Output:
2677 2767 6277 6727 7267 7627
from itertools import permutations
n=input().strip()
n=list(n)
l=[]
for i in permutations(n):
    k="".join(i)
    if int(k)%2!=0:
        l.append(int(k)) 
print(*sorted(set(l)))
