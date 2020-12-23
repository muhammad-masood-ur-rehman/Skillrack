Right Arrow Pattern Program In Python
The program must accept an odd integer N as the input. The program must print the N lines containing hyphens and asterisks based on the following conditions.
- In the line 1, the program must print (N-1)/2 hyphens followed by an asterisk.
- In the line 2, the program must print (N-1)/2 + 1 hyphens followed by an asterisk.
- In the line 3, the program must print (N-1)/2 + 2 hyphens followed by an asterisk.
- Similarly, the program must print the first (N-1)/2 lines as the output.
- In the line (N+1)/2, the program must print N asterisks.
- In the line (N+1)/2 + 1, the program must print N-2 hyphens followed by an asterisk.
- In the line (N+1)/2 + 2, the program must print N-3 hyphens followed by an asterisk.
- In the line (N+1)/2 + 3, the program must print N-4 hyphens followed by an asterisk.
- Similarly, the program must the remaining lines as the output.
Boundary Condition(s):
5 <= N <= 99
Input Format:
The first line contains N.
Output Format:
The first N lines contain the hyphens and asterisk(s) based on the conditions.
Example Input/Output 1:
Input:
5
Output:
--*
---*
*****
---*
--*
Explanation:
Here N = 5.
The 1st line contains (5-1)/2 hyphens and an asterisk.
--*
The 2nd line contains (5-1)/2 + 1 hyphens and an asterisk.
---*
The 3rd line contains 5 asterisks.
*****
The 4th line contains (5-2) hyphens and an asterisk.
---*
The 5th line contains (5-3) hyphens and an asterisk.
--*
Example Input/Output 2:
Input:
7
Output:
---*
----*
-----*
*******
-----*
----*
---*
n=int(input())
k=0;p=n
a=[]
while(True):
    l=(n-1)//2+k
    if l+1-n==0:
      break
    else:
      a.append(l*'-'+'*')
    k+=1
f=a[::-1]
a.append(n*'*')
for i in a+f:
  print(i)
