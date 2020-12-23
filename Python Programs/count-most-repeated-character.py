Count - Most Repeated Character
The program must accept a string S containing only alphanumeric characters as the input. The program must print the number of occurrences of the most repeated character in the string S. If all the characters in S occur only once, the program must print 1 as output.
Example Input/Output 1:
Input:
communication
Output:
2
Explanation:
Here the string S = communication.
The characters c, o, m, n and i each occur twice.
The characters u, a and t each occur only once.
So the number of occurrences of the most repeated character is 2.
Hence the output is 2
Example Input/Output 2:
Input:
UpToDate
Output:
1
Example Input/Output 3:
Input:
Microprogramming100
Python:
g=input().strip()
f=set(g)
n=[]
for i in f:
         n.append(g.count(i))
 print(max(n))
s=input();m=0
for ele in s:
    if s.count(ele)>m:
        m=s.count(ele) 
print(m)
s=input().strip()
li=[s.count(ele) for ele in s]
print(max(li))
s=input().strip()
li=[]
for ele in s:
  li.append(s.count(ele))
print(max(li))
s=input()
print(max([(s.count(ele)) for ele in s]))
s=input().strip()
b=[]
for ele in s:
   b.append((s.count(ele),ele))
b=sorted(b)
print(b[-1][0])
s=input().strip()
t=[(s.count(ele)) for ele in s]
print(sorted(t)[-1])
s=input()
m=0
for ele in s:
  k=s.count(ele)
  if k>m:
     m=k
print(m)
