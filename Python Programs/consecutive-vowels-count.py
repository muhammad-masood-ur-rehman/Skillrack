Consecutive Vowels Count
Given a string S1, print the count C which represents the number of times a vowel is followed by another vowel in the string S1.
Input Format:
The first line contains S1
Output Format:
The first line contains C.
Boundary Conditions:
1 <= Length of S1 <= 1000
Example Input/Output 1:
Input:
lion
Output:
1
Example Input/Output 2:
Input:
arealiouas
Output:
4
Explanation:
ea, io, ou, ua are the 4 occurrences.
s=input().strip().lower();c=0
for i in range(len(s)-1):
    if s[i] in 'aeiou' and s[i+1] in 'aeiou':c+=1
print(c)
