String Contains X and Y
The program must accept a string S as the input. The program must print yes if the string contains only the characters 'X' and 'Y' (case insensitive). Else the program must print no as the output.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line contains S.
Output Format:
The first line contains yes or no.
Example Input/Output 1:
Input:
XyxYyXx
Output:
yes
Explanation:
The string XyxYyXx contains only the characters X and Y (case insensitive).
So yes is printed.
Example Input/Output 2:
Input:
zyxxy
Output:
no
Python :
cha="xy"
stri=input().strip()
c1,c2=0,0
for ele in stri:
      if ele.lower() in stri:
        c1=c1+1 
      else:
        c2=c2+11 
if c2!=0:
    print("no")
else:
    print("yes")
cha=input().strip()
lis=[ele for ele in a.lower()]
lis=sorted(list(set(lis)))
if 'x' in lis: remove ('x')
if 'y' in lis: remove ('y')
else: print("no")
cha=input().lower()
data=list(set(cha))
test,s=0,0
for I in data:
    if I=='x' or I=='y':
        s=s+1 
    else:
        test=test+1 
if s>=1 and test==0:
    print("yes")
else:
    print("no")
cha=input()
cnt=1
for ele in cha:
    if ele not in "xyXY":
        print("no")
        cnt=0
        break;
if(cnt==1):
    print("yes")
C:
#include<stdio.h>
int main() {
char stri[1001];
scanf("%s",stri);
for(int ele=0;ele<strlen(stri);ele++)
 {
     if(stri[ele]!='x'&&stri[ele]!='X'&&stri[ele]!='Y'&&stri[ele]!='y')
     {
         printf("no");
         return 0;
     }
}
printf("yes");
}

@ Agent Marvel
