Python Program To Find Sub-strings at least K vowels
A string S of length L and an integer K is passed as the input. The program must sort and print the count of all the unique sub-strings (with a given combination of characters) containing at least K vowels. Then the program must also print those sub-strings in sorted order.
Boundary Condition(s):
1 <= L <= 25
K <= L
Input Format:
The first line contains S.
The second line contains K.
Output Format:
The first line contains the integer value C representing the count.
Next C lines contain the sub-string values.
Example Input/Output 1:
Input:
apple
2
Output:
8
ae
ale
ape
aple
appe
apple
Explanation:
These 8 sub-strings contain at least 2 vowels (As K=2).
ela and eal are not printed as ale contains the combination of these characters.
Example Input/Output 2:
Input:
management
4
Output:
64
aaee
aaeen
aaeent
aaeet
aaeme
aaemen
aaement
aaemet
aagee
aageen
aageent
aageet
aageme
aagemen
aagement
aagemet
anaee
anaeen
anaeent
anaeet
anaeme
anaemen
anaement
anaemet
anagee
anageen
anageent
anageet
anageme
anagemen
anagement
anagemet
maaee
maaeen
maaeent
maaeet
maaeme
maaemen
maaement
maaemet
maagee
maageen
maageent
maageet
maageme
maagemen
maagement
maagemet
manaee
manaeen
manaeent
manaeet
manaeme
manaemen
manaement
manaemet
managee
manageen
manageent
manageet
manageme
managemen
management
managemet
from itertools import combinations as c 
s=input().strip()
f=[]
n=int(input())
for i in range(1,len(s)+1):
    for j in list(c(s,i)):
        p=0 
        for h in j:
            if h in 'aeiouAEIOU':
                p+=1 
        if p>=n and ''.join(j) not in f:
            f.append(''.join(j))
print(len(f))
for i in sorted(f):
    print(i)
