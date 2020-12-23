Alphabets and Sum of Digits
The program must accept a string S containing only alphabets and digits as the input. The program must print the alphabets and then the sum of the digits in the string S as the output.
Note: At least one alphabet and one digit are always present in the string S.
Python Interview Questions
Example Input/Output 1:
Input:
A1B2c3d4E5
Output:
ABcdE15
Explanation:
The alphabets in the string A1B2c3d4E5 are A, B, c, d and E. So they are printed.
The digits in the string A1B2c3d4E5 are 1, 2, 3, 4 and 5. So their sum 15 is printed.
Example Input/Output 2:
Input:
SkillRack314
Output:
SkillRack8
C++:
#include <iostream>
#include<cstring>
using namespace std;
int main(int argc, char** argv)
{
char string[1001];
cin>>string;
int sum=0,i;
for(i=0;i<strlen(string);i++)
{
    if(isalpha(string[i]))
    cout<<string[i];
    else
    sum+=string[i]-'0';
}
cout<<sum;
}
Python:
s=input().strip()
c=0
d=" "
for i in s:
    if i.isalpha():
       d+=i 
    if i.isdigit():
       c+=int(i)
print(d+str(c))
alpha=input().strip() 
beta="0123456789"
str=''
a=0 
for ele in alpha: 
    if ele in beta:
        a+=int(ele) 
    else: 
        str+=ele
print(str,end="")
print(a)
alpha=input().strip() 
beta="1234567890" 
p=[]
q=[] 
for ele in alpha: 
    if ele not in beta:
        p.append(ele) 
    else: 
        q.append(int(ele))
print(*p,sum(q),sep="")
alpha=input().strip()
b='';c=0
for ele in alpha:
   if ele in '0123456789':
      c+=int(ele)
   else:
      b+=ele 
print(b+str(c))
Java:
import java.util.*;
public class Hello {
public static void main(String[] args) { 
Scanner sc=new Scanner(System.in); 
String s=sc.nextLine(); 
int c=0; 
for(int i=0;i<s.length();i++){ 
char a=s.charAt(i); 
if(Character.isDigit(a)){ 
int b=Integer.parseInt(String.valueOf(a)); 
c+=b;
}
else System.out.print(a);
}
System.out.println(c);
C:
#include<stdio.h>
#include <stdlib.h>
int main()
{
char input[1001];
int index,sum=0,len;
scanf("%s",input);
len=strlen(input);
for(index=0;index<len;index++)
{
    if(isdigit(input[index]))
    sum+=input[index]-'0';
    else
    printf("%c",input[index]);
}
printf("%d",sum);
}
#include<stdio.h>
#include <stdlib.h>
int main()
{
    int sum=0;
    char str[1000];
    scanf("%s",str);
    for(int i=0;str[i];++i){
        if(isdigit(str[i])){
            sum+=str[i]-'0';
        }
        else{
            printf("%c",str[i]);
        }
    }
    printf("%d",sum);
}
