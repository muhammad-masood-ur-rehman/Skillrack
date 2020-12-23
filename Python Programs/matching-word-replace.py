Matching Word - Replace ?
The program must accept two string values P and S as input. The string P represents a pattern. The string S represents a set of words. The character '?' in P matches any single character. The program must print the word in S that matches the given pattern P as the output. If two or more words match the pattern P, then the program must print the first occurring word as the output.
Note: At least one word in S is always matched with P.
Boundary Condition(s):
1 <= Length of P <= 100
1 <= Length of S <= 1000
Input Format:
The first line contains P.
The second line contains S.
Output Format:
The first line contains a string representing the word in S that matches the pattern P.
Example Input/Output 1:
Input:
?i?n
LION crane lion breath kiln
Output:
lion
Explanation:
Here P = "?i?n" and S = "LION crane lion breath kiln".
There are two words in S that match the pattern P.
lion klin
So the first occurring word lion is printed as the output.
Example Input/Output 2:
Input:
BR??E?
BRIGHT BEST BRAVE BROKEN
Output:
BROKEN
s=input().strip()
k=s;p=[];m=0
l=input().strip().split()
for i in l:
    m=0
    if len(i)==len(s):
        for j in range(len(i)):
            if s[j]!='?' and s[j]!=i[j]:
                m=1
        if m==0:
            p.append(i)
print(p[0])
