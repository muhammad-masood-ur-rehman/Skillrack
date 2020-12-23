Number Sequence Sort
The program must accept and sort N number sequences. A number sequence can be multiplication, power or a normal number. The sorted list should be printed in it's original form.
Boundary Condition(s):
Length of the the number sequence is from 1 to 100
1 <= N <= 20
Input Format:
The first line contains N.
The next N lines contain the N number sequences.
Output Format:
N lines contain the number sequences sorted in ascending order based on their resulting values.
Example Input/Output 1:
Input:
4
2^2^2^2
3^4
35
20*3
Output:
35
20*3
3^4
2^2^2^2
Explanation:
2^2^2^2 = 256
3^4= 81
35 = 35
20*3 = 60
So sorting them in ascending order, we get 35 60 81 256. Now their original form is printed for these values in consecutive lines.
import re
n=int(input())
l=[]
for ele in range(n):
    s=input().strip()
    l1=list(map(int,re.findall("[\d]+",s)))
    l2=list(re.findall("[^\d]",s))
    a=l1[0]
    j=1
    for i in l2:
        if i=='^':
            a=a**l1[j]
        elif i=='*':
            a=a*l1[j]
        j+=1
    l.append([s,a])
l.sort(key=lambda a:a[1])
for i in l:
    print(i[0])
