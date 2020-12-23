Anagrams Count
Two strings S1, S2 are passed as input to the program. The program must print the count of anagrams present in both the strings. Out of each pair of words in the anagram the first word in the pair must be in S1 and the second word in the pair must be in S2.
If two words have the same characters and the occurrence number of each character is also identical respectively, they are anagrams.
Example:  silent & listen
Input Format:
The first line will contain the value of S1.
The first line will contain the value of S2.
Boundary Conditions:
Length of S1 and S2 is from 5 to 200.
Output Format:
The count of pair of anagrams in S1 and S2 based on the conditions mentioned.
Example Input/Output 1:
Input:
but i will not listen to him
water dropped into the silent tub
Output:
2
Explanation:
The anagram pairs are
but tub
listen silent
Example Input/Output 2:
Input:
please dear agree to take kids outside
if you are eager read and skid
Output:
3
Explanation:
The anagram pairs are
dear read
agree eager
kids skid
Example Input/Output 3:
Input:
heavy weight dice iced
cast medicine iron
Output:
0
Explanation:
There are no anagram pairs (as dice and iced are in the same string)
s=input().split();a=[];l=[];c=0
d=input().split();b=[];m=[]
for i in s:a.append(sorted(i))
for i in a:
  k=''
  for j in i:k+=j
  l.append(k)
for i in d:b.append(sorted(i))
for i in b:
  p=''
  for j in i:p+=j
  m.append(p)
for i in l:
  if i in m:c+=1
print(c)
