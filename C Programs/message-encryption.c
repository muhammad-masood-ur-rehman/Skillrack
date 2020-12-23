Message Encryption
To encrypt messages Jil will first decide on the number of columns C to use. Then Jil will pad the message with letters chosen randomly so that they form a rectangular matrix. Finally Jil will write down the message navigating the rows from left to right and then from right to left.
The program must accept the encrypted message M as input and then extract and print the original message (along with any additional padding letters) from the encrypted one based on the value of C.

Boundary Conditions:
Length of M is from 4 to 200.
2 <= C <= 20

Input Format:
First line will contain the string value of the encrypted message M.
Second line will contain the integer value of the column used for the encryption.
Output Format:
First line will contain the string value of the original message (along with any additional padding letters)

Sample Input/Output:
Example 1:
Input:
midinadiazne
3
Output:
madeinindiaz
Explanation:
m i d
a n i
d i a
e n z
Here z is the padding letter. The navigating across the rows mid (left to right) ina (right to left) and so on we come up with the encrypted message midinadiazne.

Example 2:
Input:
loaesfbnaiordilertenrdhdw
5
Output:
lionroaredandthebirdsflew
Explanation:
l o a e s
i a n b f
o r d i l
n e t r e
r d h d w
Here there are no padding letters. The navigating across the rows left to right and then from right to left we get loaesfbnaiordilertenrdhdw
a=input().strip()
n=int(input())
l=[];k=0;p=[]
for i in range(0,len(a),n):
    if i%2==0:l.append(a[i:i+n])
    else:l.append(a[i:i+n][::-1])
for i in range(n):
    f=''
    for j in l:f+=j[k]
    p.append(f);k+=1 
print(''.join(p))
#include<stdio.h>
#include <stdlib.h>

int main()
{
 char str[1000];
 char arr[100][100];
 scanf("%s",str);//getting the string
 int col,count=0,j;
 scanf("%d",&col);//coloumn value
 int row=strlen(str)/col;//row value
 
 for(int i=0;i<row;i++)
 {
 if(i%2==0)//odd in straight order
 for( j=0;j<col;j++)
 {
 arr[i][j]=str[count];
 count++;
 }
 
 else//even in reverse order
 for(j=col-1;j>=0;j--)
 {
 arr[i][j]=str[count];
 count++;
 }
 }
 
 for(int i=0;i<col;i++)
 {
 for(j=0;j<row;j++)
 {
 printf("%c",arr[j][i]);//display the string
 }
 
 }
}
