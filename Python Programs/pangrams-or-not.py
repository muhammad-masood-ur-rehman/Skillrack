Pangrams or not
Pengrams are words or sentences containing every letter of the English alphabet at the most once. Write an algorithm and  a subsequent Python code to check whether a string is a pengram or not. Write a function to check if a given string is a pengram. For example, "He is at work" is a pengram. Since every letter of the english alphabet occurs at the most once.
def pengram(word):
 p=list(word)
 p=list(filter(lambda a: a != ' ', p))
 flag=0
 for i in p:
  if(p.count(i)>1):
   flag=1
   break
 if(flag==0):
  print('yes')
 else:
  print('no')

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
