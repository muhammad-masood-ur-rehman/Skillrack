Reverse String - Vowels Retain Same Position
Given a string S1 as the input, the program must reverse the string, keeping the vowels in the same position.
Input Format:
The first line contains S1
Output Format:
The first line contains S1 reversed with vowels retaining the same position.
Boundary Conditions:
1 <= Length of S1 <= 1000
Example Input/Output 1:
Input:
abhcezjqu
Output:
aqjzechbu
#include <algorithm>
#include <ctype.h>
#include <iostream>
#include <string.h>
using namespace std;

char v[] = {'a', 'e', 'i', 'o', 'u'};
bool vowel(char c) {
	c = tolower(c);
	return (find(v, v + 5, c) != v + 5);
}
int main(int argc, char **argv) {
	char s[1001];
	cin >> s;
	int l = strlen(s);
	int i = 0, j = l - 1;
	while (i <= j) {
		if (!(vowel(s[i]) || vowel(s[j]))) {
			char temp = s[i];
			s[i] = s[j];
			s[j] = temp;
			i++;
			j--;
		}
		if (vowel(s[i])) {
			i++;
		}
		if (vowel(s[j])) {
			j--;
		}
	}
	cout << s;
}
#include <iostream>
#include<string.h>
using namespace std;

int main(int argc, char** argv)
{
char a[101],ch;
cin>>a;
int i=0,j=strlen(a)-1;
while(i!=j){
    if(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u'){
        i++;
    }
    else{
        if(a[j]=='a'||a[j]=='e'||a[j]=='i'||a[j]=='o'||a[j]=='u'){
            j--;
        }
        else{
            ch=a[i];
            a[i]=a[j];
            a[j]=ch;
            i++;j--;
        }
    }
}
cout<<a;
}
