Alternate Lower Case & Upper Case
Alternate Lower Case & Upper Case: The program must accept a string S and print the first N lower case alphabets and the first N upper case alphabets alternatively.
Note: At least N lower case alphabets and N upper case alphabets are always present in the string S.
Boundary Condition(s):
2 <= Length of S <= 1000
1 <= N <= 100
Input Format:
The first line contains S.
The second line contains N.
Output Format:
The first line contains the first N lower case alphabets and the first N upper case alphabets alternatively.
Example Input/Output 1:
Input:
abAdCplaNE
2
Output:
aAbC
Example Input/Output 2:
Input:
cRICkEt
3
Output:
cRkItC
s=input().strip();a='';b=''
n=int(input());c=0;d=0
for i in s:
  if i.islower() and c<n:a+=i;c+=1 
for i in s:
  if i.isupper() and d<n:b+=i;d+=1
for i in range(max(len(a),len(b))):
  if i<len(a):print(a[i],end='')
  if i<len(b):print(b[i],end='')
