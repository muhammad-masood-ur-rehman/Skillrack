Interlace Vowels & Consonants
The program must accept a string S containing only alphabets as the input. The program must print all the vowels in the string S in the order of their occurrence interlaced with all the consonants in the string S in the reverse order of their occurrence as the output.
Boundary Condition(s):
1 <= Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains the string value as per the given condition.
Example Input/Output 1:
Input:
SkillRack
Output:
ikacRllkS
Explanation:
The vowels in the string SkillRack are i and a.
The consonants in the string SkillRack are S, k, l, l, R, c and k.
After interlacing the vowels (in the order of their occurrence) with the consonants (in the reverse order of their occurrence), the string becomes ikacRllkS.
So ikacRllkS is printed as the output.
Example Input/Output 2:
Input:
Heaven
Output:
enaveH
Example Input/Output 3:
Input:
AEIOU
Output:
AEIOU
Python:
strin=input().strip()
c=""
v='' 
for ele in strin:
    if ele in "aeiouAEIOU":
        var+=ele
    else:
        ctr+=ele
ctr=ctr[::-1]
ele=0
while ele<min(len(ctr),len(var)):
    print(var[ele]+ctr[ele],end="")
    ele+=1
print(ctr[ele:]+var[ele:])
C:
#include<stdio.h>
#include <stdlib.h>
int isvowel(char c)
{
    c=tolower(c);
    if(c=='a' || c=='e' || c=='ele' || c=='o' || c=='u')
    return 1;
    else
    return 0;
}
int main()
{
char strin[1001];
scanf("%s",strin);
char var1[1001],var2[1001];
int bar=0,l=0;
for(int ele=0;ele<strlen(strin);ele++)
{
    if(isvowel(strin[ele]))
    {
        var1[bar++]=strin[ele];
    }
    else
    {
        var2[l++]=strin[ele];
    }
}
int foo=0;
while(foo<bar || l>0)
{
    if(foo<bar)
    {
        printf("%c",var1[foo]);
        foo++;
    }
    if(l>0)
    printf("%c",var2[--l]);
}

}
C++:
#include <bits/stdc++.h>
 using namespace std;
int main(int argc, char** argv)
{
    string strin,vow="",cons=""; 
    cin>>strin; 
    for(int ele=0;ele<strin.size();ele++){
        char ch=tolower(strin[ele]);
        if(ch=='a' || ch=='e' || ch=='ele' || ch=='o' || ch=='u'){
            vow+=strin[ele];
        }
        else{
            cons+=strin[ele];
        }
    }
    cons=string(cons.rbegin(),cons.rend());
    for(int ele=0;ele<max(vow.size(),cons.size());ele++){
        if(ele<vow.size()){
            cout<<vow[ele]<<"";
        }
        if(ele<cons.size()){
            cout<<cons[ele];
        }
    }
}
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		String a=s.nextLine();
		String vowels="",consonants="";
		for(char c:a.toCharArray()){
		    char x=Character.toLowerCase(c);
		    if(x=='a' || x=='e' || x=='i' || x=='o' || x=='u')
		        vowels+=c;
		    else 
		        consonants+=c;
		}
		int i=0,j=consonants.length()-1;
		while(i<vowels.length() || j>=0){
		    if(i<vowels.length())
		        System.out.print(vowels.charAt(i++));
		    if(j>=0)
		        System.out.print(consonants.charAt(j--));
		}
	}
}
