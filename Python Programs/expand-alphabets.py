Expand Alphabets
Expand Alphabets: Given a string S with alphabets and their count, repeat the alphabets based on their count and print the value as the output.
Input Format:
The first line contains S.
Output Format:
The first line contains the alphabets repeated based on their count.
Boundary Condition:
1 <= Length of S <= 100
Example Input/Output 1:
Input:
a2c5z4
Output:
aaccccczzzz
s=input().strip()
a=[];b=[]
o=''
for i in s:
    if i.isdigit():
        o+=i
    else:
        a.append(i)
        if o!='':
            b.append(o)
            o=''
b.append(o)
for i in range(len(a)):
    print(a[i]*int(b[i]),end='')
