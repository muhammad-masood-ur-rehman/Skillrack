Maximum Uncommon Characters
Maximum Uncommon Characters: Given N strings as input, the program must print the string which has the maximum number of uncommon characters. If more than one strings have the same number of uncommon characters print the first occurring string.
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains the value of N.
The N lines contain a string each.
Output Format:
The first line contains a string.
Example Input/Output 1:
Input:
4
tiger
umbrella
power
killer
output:
umbrella
Explanation:
The common characters are e and r.
The uncommon characters are (t i g), (u m b l l a), (p o w), (k i l l).
Hence umbrella is the output.
Example Input/Output 2:
Input:
3
aaayz
yzbcd
cceyz
output:
aaayz
Explanation:
The common characters are y and z.
The uncommon characters are (a a a), (b c d), (c c e).
Hence aaayz is the output.
a=int(input()) 
b=[] 
for i in range(a):
    b.append(*input().split())   
s=b[0] 
ans=[] 
if a==1:
    print(s)
    exit()
for i in s:  
    c=0  
    f=0
    for j in range(1,a):  
        if i in b[j]:
            f+=1   
            break
    if(f==a-1):
        ans.append(i)  
maxi=0
for i in b: 
    count=0
    for j in i:
        if j not in ans:
            count+=1 
    if count>maxi:
        maxi=count 
        string=i
print(string)
