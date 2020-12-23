String Alphabet Count
String Alphabet Count: Given a string S with only alphabets, print the alphabet and it's count as shown in the Example Input/Output section.
Input Format:
The first line contains S.
Output Format:
The first line contains the alphabet and it's count as shown in the Example Input/Output section.
Boundary Condition:
1 <= Length of S <= 100
Example Input/Output 1:
Input:
apple
Output:
a1 e1 l1 p2
s=sorted(input())
k=''
for i in s:
    if i not in k:
        k+=i 
for i in k:
    print(i,s.count(i),sep='',end=' ')
