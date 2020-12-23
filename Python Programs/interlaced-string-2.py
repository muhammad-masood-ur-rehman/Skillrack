Interlaced String
Given two strings S1 and S2 as input, the program must print the characters of the second string from the last interlaced with the characters of the first string from first as shown in Example Input/Output Section.
Boundary Condition(s):
1 <= Length of each string <= 100
Input Format:
The first line contains the string S1.
The second line contains the string S2.
Output Format:
The first line contains the interlaced string.
Example Input/Output 1:
Input:
abcde
fghij
Output:
jaibhcgdfe
Example Input/Output 2:
Input:
abcd
efghijk
Output:
kajbichdgfe
a=input().strip()
b=input().strip()[::-1]
c=max(len(a),len(b))
for i in range(c):
    if i<len(b):
        print(b[i],end="")
    if i<len(a):
        print(a[i],end="")
