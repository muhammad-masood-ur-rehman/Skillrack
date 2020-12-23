Same Unique Characters or Not
The program must accept two string values S1 and S2 containing only lower case alphabets as the input. The program must print yes if the given two string values contain the same unique alphabets. Else the program must print no as the output.
Example Input/Output 1:
Input:
google
lego
Output:
yes
Explanation:
The unique alphabets in the string google are g, o, l and e.
The unique alphabets in the string lego are l, e, g and o.
Here the given two string values contain the same unique alphabets. So yes is printed as the output.
Example Input/Output 2:
Input:
pot
post
Output:
no
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
int i,hash1[26]={0},hash2[26]={0};
char s1[101],s2[101];
scanf("%s %s",s1,s2);
for(i=0;i<strlen(s1);i++)
hash1[s1[i]-'a']=1;
for(i=0;i<strlen(s2);i++)
hash2[s2[i]-'a']=1;
for(i=0;i<26;i++)
if(hash1[i]!=hash2[i])
{
    printf("no");
    return 0;
}
printf("yes");
}
Python:
word1=sorted(list(set(input().strip())))
word2=sorted(list(set(input().strip()))) 
if word1==word2:
   print('yes') 
else:
   print('no')
S1=input().strip()
S2=input().strip()
if sorted(set(S1))==sorted(set(S2)):
     print("yes")
else:
     print("no")
S1=set(input().strip())
S2=set(input().strip())
if S1==S2: print("yes")
else: print("no")
string1=input().strip()
string2=input().strip()
substr1=sorted(string1)
substr2=sorted(string2)
print('yes' if set(substr1)==set(substr2) else 'no')
Java
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        String s1=scan.next(),s2=scan.next();
        int hash1[]=new int[26];
        int hash2[]=new int[26];
        
        for(char ch:s1.toCharArray()){
            hash1[ch-'a']=1;
        }
        for(char ch:s2.toCharArray()){
            hash2[ch-'a']=1;
        }
        for(int i=0;i<26;++i){
            if(hash1[i]!=hash2[i]){
                System.out.print("no");
                return;
            }
        }
        System.out.print("yes");
	}
}
