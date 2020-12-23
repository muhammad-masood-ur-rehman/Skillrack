Four Strings Square
Four Strings Square: Four strings all having the same length L are passed as the input to the program. The four strings must be printed in a L*L square matrix shape as shown in the example input/output.
The string which is on the top will always be the first string in the input. Other three strings can occur in a random order in the input. The sequence of the string can be identified by the fact that the last letter of a string will be the first letter of another string (and you can safely assume the last letter will not occur more than once).
Input Format:
The first line contains the string which represents the top of the square matrix.
The next three lines will contain the remaining the three string values which can represent the right, left and bottom side of the squares, but not necessarily in the same order.
Output Format:
The L*L square matrix with these four strings as it's sides as described in the Example Input/Output.
Boundary Conditions:
3 <=  L <= 100
Example Input/Output 1:
Input:
TIGER
YACHT
RANGE
EVERY
Output:
TIGER
H***A
C***N
A***G
YREVE
Example Input/Output 2:
Input:
MAN
DOT
NOD
TIM
Output:
MAN
I*O
TOD
a=input().strip()
b=input().strip()
c=input().strip()
d=input().strip()
p=[]
p.append(a)
if a[0]==b[-1]:
    x=b
elif a[0]==c[-1]:
    x=c
else:
    x=d
if a[-1]==b[0]:
    y=b
elif a[-1]==c[0]:
    y=c
else:
    y=d
if b[0]!=a[-1] and b[-1]!=a[0]:
    z=b
elif c[0]!=a[-1] and c[-1]!=a[0]:
    z=c
else:
    z=d
x=x[1:len(x)-1][::-1]
y=y[1:len(y)-1]
for i in range(len(x)):
  l=[]
  l.append(x[i])
  l.append((len(a)-2)'')
  l.append(y[i])
  p.append(l)
for i in p:
  for j in i:
      print(j,end='')
  print()
print(z[::-1])
#include<iostream>
#include<string>
#include<vector>
using namespace std;
 
int main()
{
    int l,i,j;
    string s1,s2,s3,s4;
    cin>>s1>>s2>>s3>>s4;
    l = s1.size();
    vector <string> words;
    words.push_back(s1);
    while(words.size() < 4)
    {
        string lastWord = words[words.size()-1];
        char lastLetter = lastWord[lastWord.size()-1];
        if(s2[0] == lastLetter)
            words.push_back(s2);
        else if(s3[0] == lastLetter)
            words.push_back(s3);
        else if(s4[0] == lastLetter)
            words.push_back(s4);
    }
    char pattern[l][l];
    for(i=0; i<l; i++)
    {
        for(j=0; j<l; j++)
        {
            pattern[i][j] = '*';
        }
    }
   
    for(i=0; i<l; i++)
        pattern[0][i] = words[0][i];
    for(i=0; i<l; i++)
        pattern[i][l-1] = words[1][i];
    for(i=0; i<l; i++)
        pattern[l-1][i] = words[2][l-i-1];
    for(i=0; i<l; i++)
        pattern[i][0] = words[3][l-i-1];
    for(i=0; i<l; i++)
    {
        for(j=0; j<l; j++)
        {
            cout<<pattern[i][j];
        }
        cout<<endl;
    }
    return 0;
}
