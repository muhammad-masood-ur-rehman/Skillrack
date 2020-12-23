FLAMES Game
FLAMES game is a relationship calculating game. Letters in FLAMES stand for,
F - FRIENDS
L - LOVER
A - AFFECTION
M - MARRIAGE
E - ENEMY
S - SIBLING
Calculation Logic - FLAMES:
1. Get two names S1 and S2.
2. Remove the common characters in both the names.
3. Find the count of the characters that are left, the count is called FLAMES count FC.
4. Consider FLAMES letters ('F', 'L', 'A', 'M', 'E', 'S') and start removing the letters in a circular manner using the FC.
5. The letter which is finally left desides the output, If it's
F - FRIENDS
L - LOVER
A - AFFECTION
M - MARRIAGE
E - ENEMY
S - SIBLING
Input Format:
First line contains S1
Second line contains S2
Output Format:
First line contains FLAMES relationship in uppercase.
Boundary Conditions:
2 <= S1, S2 <= 100
Example Input/Output 1:
Input:
raja
rani
Output:
ENEMY
Example Input/Output 2:
Input:
waffles
bright
Output:
AFFECTION
a=input().strip().lower()
b=input().strip().lower()
flames=['FRIENDS', 'LOVER', 'AFFECTION', 'MARRIAGE', 'ENEMY', 'SIBLING']
for i in a:
    for j in b:
        if i==j:
            a=a.replace(i,"",1)
            b=b.replace(i,"",1)
fc=len(a+b)
while len(flames)>1:
    si=(fc%len(flames))-1
    if si>=0:
        r=flames[si+1:]
        l=flames[:si]
        flames=r+l
    else:
        flames=flames[:len(flames)-1]
print(*flames)
