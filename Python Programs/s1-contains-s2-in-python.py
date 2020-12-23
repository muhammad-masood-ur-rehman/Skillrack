S1 Contains S2 In Python
S1 Contains S2 In Python: Given two string values S1 and S2, the program must print YES if the characters of S2 occurs in the same order of occurrence in the string value S1. (The characters of S2 need not to be continuous but maintain their relative order). Else the program must print NO.
Boundary Condition(s):
1 <= Length of S1, S2 <= 10^7
Input Format:
The first line contains the string S1.
The second line contains the string S2.
Output Format:
The first line contains either YES or NO.
Example Input/Output 1:
Input:
superkoolfillerandcopperkit
skillrack
Output:
YES
Explanation:
skillrack is present in the same order of occurrence in S1 in the following positions. Hence the output is YES.
s-1 k-6 i-11 l-12 l-13 r-15 a-16 c-19 k-25
Example Input/Output 2:
Input:
germanactor
men
Output:
NO
a=input().strip()
b=input().strip()
k=0
l=[]
if a[0]==b[0]:
    l.append(1)
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j] and j>k:
            l.append(j+1)
            k=j 
            break
if len(l)==len(b):
    print("YES")
else:
    print("NO")
