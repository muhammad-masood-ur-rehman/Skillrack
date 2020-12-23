Chars To Remove For Same String Value
N string values S1, S2, S3, SN are passed as input to the program. Values of S1, S2, S3, SN are such that if one character is removed from each of these string values, then the resulting string values are equal (same).
The characters to be removed from the string values named C1, C2, C3, CN  will be different for each string.

Input Format:
The first line will contain the value of N.
The next N lines will contain the values of strings S1 to SN.
Boundary Conditions:
2 <= N <= 10
Length of string SN is from 2 to 200
Output Format:
The first line will contain the characters C1, C2, C3, .. CN to be removed from each of these string without any space between them.

Example Input/Output 1:
Input:
2
bmanabgerb
manasgsesr
Output:
bs
Explanation:
If the character b is removed from the first string, it becomes manager.
If the character s is removed from the second string, it becomes manager.
Hence bs is printed as output.

Example Input/Output 2:
Input:
5
abcdef
ambcde
qabcdqe
kkakbkckdke
zabczdzzze
Output:
fmqkz
Python:
n=int(input())
lth='';b=[]
l=[input().strip() for i in range(n)]
for i in range(len(l)):
    if len(lth)<len(l[i]):
       lth=l[i]
w=l[l.index(lth)]
r='';r2=''
for i in w:
    c=0 
    for j in l:
        if i in j:c+=1
    if c==n:r+=i 
for i in l:
    for j in i:
        if j not in r and j not in r2:
           r2+=j
print(r2)
a=int(input()) 
b=[]  
for i in range(a):
    dd=input().split()
    b.append(*dd)
jj=b[0] 
c=[] 
d=[]
for i in range(1,a): 
    s=""
    for j in range(len(b[i])):
        if b[i][j] in jj:
            s+=b[i][j]  
    c.append(s)  
    ss="" 
    for j in range(len(b[i])):
        if b[i][j] not in s and b[i][j] not in ss:
            ss+=b[i][j]
    d.append(ss)   
sss="" 
for i in jj:
    if i not in c[0] and i not in sss:
        sss+=i
print(sss,end="") 
for i in d:
    print(i,end="")
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
 int ele,foo,n;
 int arr[1000]={0},arr1[1000]={0};
 scanf("%d\n",&n);
 char strin[1000],s1,s2;
 scanf("%strin",strin);
 for(ele=0;ele<strlen(strin);ele++)
 arr[strin[ele]]++;
 for(ele=1;ele<n;ele++)
 {
     scanf("%strin",strin);
     int arr1[1000]={0};
     for(foo=0;foo<strlen(strin);foo++)
     {
        arr1[strin[foo]]++;
     }
     for(foo=96;foo<=122;foo++)
     {
         if(ele==1)
         {
             if(arr1[foo]!=arr[foo])
             {   
                 if(arr1[foo]>arr[foo]) 
                 s2=foo;
                 else
                 {
                 s1=foo;
                 arr[foo]=arr1[foo];
                 }
             }
         }
         else 
         {
             if(arr1[foo]!=arr[foo])
             printf("%c",foo);
         }
     }
     if(ele==1)
     printf("%c%c",s1,s2); 
 }
}
