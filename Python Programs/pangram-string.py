Pangram String
A string S is passed as the input to the program. If S is a pangram, the program must print yes else it must print no. Uppercase and lower case letters of an alphabet are considered the same.
Pangram definition from WikiPedia: A Pangram (Greek: pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a sentence using every letter of the alphabet at least once.
Input Format:
The first line contains S
Output Format:
The first line contains the value yes or no depending on whether S is a pangram or not.
Boundary Conditions:
5 <= Length of S <= 1000
Example Input/Output 1:
Input:
Five jumping wizards hex bolty quick
Output:
yes
Example Input/Output 2:
Input:
abcdefghijklqrstuvwxyz
Output:
no
Explanation:
The alphabets mnop are not present.
def pengram(word):
 p=list(word)
 p=list(filter(lambda a: a != ' ', p))
 flag=0
 for i in p:
  if(p.count(i)>1):
   flag=1
   break
 if(flag==0):
  print('no')
 else:
  print('yes')

w=input().lower()
pengram(w)
n=input().rstrip()
l=[]
for i in n :
    if i.isalpha() :
        i=i.lower()
        if i not in l :
            l.append(i)
if len(l)==26 :
    print('yes')
else :
    print('no')
#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{

string s;
getline(cin,s);
int a[26] = {0};

for(int i=0;i<s.length();i++)
{
    if(s[i] <= 90 && s[i] >= 65)
    {
        a[s[i]-65]++;
    }
    else
    {
        a[s[i]-97]++;
    }
}

for(int i=0;i<26;i++)
{
    if(a[i] == 0)
    {
        cout << "no";
        return 0;
    }
}

cout << "yes";
}
