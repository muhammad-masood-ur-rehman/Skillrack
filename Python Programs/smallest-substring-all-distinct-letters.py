Smallest Substring - All Distinct Letters
A string value S containing only alphabets (both lower and upper case) is passed as input to the program. The program must print the size of the smallest substring which contains all the distinct alphabets in the string S.
Input Format:
First line contains S.
Output Format:
First line contains the size of the smallest substring which contains all the distinct characters in the string S.
Boundary Conditions:
1 <= Length of string S <= 1000
Note:
a and A (lower and upper case letters are considered different). Hence the string aAaaA contains 2 distinct alphabets.
Example Input/Output 1:
Input:
abcdfffccbbfeaad
Output:
8
Explanation:
The smallest sub string that contains all the distinct letters is cbbfeaad whose length is 8.
Example Input/Output 2:
Input:
klLDKFFKpPoOGAFSGxxkllhaJSHJAlqadyASFLHJASHFA
Output:
32
Explanation:
The smallest sub string that contains all the distinct letters is LDKFFKpPoOGAFSGxxkllhaJSHJAlqady whose length is 32.
string=str(input().strip())
l=[]
for i in range(len(string)):
    if string[i] not in l:
        l.append(string[i])
minima=9999
for i in range(len(string)):
    l2=[]+l[:]
    k=-1
    for j in range(i,len(string)):
        if string[j] in l2:
            l2.remove(string[j])
        if l2==[]:
            k=j
            break
    if k!=-1:
        temp=k-i
        if temp<minima:
            minima=temp
print(minima+1)
