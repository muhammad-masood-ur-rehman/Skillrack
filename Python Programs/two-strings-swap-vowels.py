Two Strings - Swap Vowels
Two Strings - Swap Vowels: The program must accept two string values S1 and S2 as the input. The program must swap vowels in the first string with vowels in the second string in the order of their occurrences. Then the program must print the modified string values as the output.
Boundary Condition(s):
1 <= Length of S1 and S2 <= 1000
Input Format:
The first line contains S1.
The second line contains S2.
Output Format:
The first line contains modified S1.
The second line contains modified S2.
Example Input/Output 1:
Input:
environment
auditorium
Output:
anvurinmont
eidoterium
Explanation:
The vowels in the first string (environment) in the given order are e, i, o and e.
The vowels in the second string (auditorium) in the given order are a, u, i, o, i and u.
These vowels are swapped in both the string values in the given order.
So the two string values become anvurinmont and eidoterium.
The string S2 has two vowels more than the string S1 which are not swapped.
Example Input/Output 2:
Input:
pen
basket
Output:
pan
besket
s=list(input().strip());x=0;y=0
d=list(input().strip());a=[];b=[]
a=[i for i in s if i in 'aeiou']
b=[i for i in d if i in 'aeiou'];k=min(len(a),len(b))
for i in range(len(s)):
  if s[i] in 'aeiou' and x<k:s[i]=b[x];x+=1 
  print(s[i],end='')
print()
for i in range(len(d)):
  if d[i] in 'aeiou' and y<k:d[i]=a[y];y+=1 
  print(d[i],end='')
