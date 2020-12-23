Sum of Embedded Numbers
String S is passed as the input to the program. S will have positive numbers in it along with other characters. The program must print the sum of all numbers embedded in the string.
Input Format:
The first line contains S
Output Format:
The first line contains the sum of all numbers in S.
Boundary Conditions:
5 <= Length of S <= 1000

Example Input/Output 1:
Input:
kilo100gram555dhal900
Output:
1555
Example Input/Output 2:
Input:
65rich100guys70went100to22park
Output:
357
a=input().strip()
b=[]
s=""
for i in a:
    if i.isdigit():
        s+=i 
    else:
        if s:
            b+=[int(s)]
            s=""
if s:
    b+=[int(s)]
print(sum(b))
#include<iostream>
#include<string>
using namespace std;
int sum(string str) {
	int i=0,j=0,s=0,sum=0;
	int arr[100];
	for(i=0;i<str.size();) {
		char ch=str[i];
		if(ch>='a' && ch<='z') {
			i++;
			if(j!=0){
				for(int k=0;k<j;k++)
					s=s*10+arr[k];
				sum+=s;
			}
			j=0;
			s=0;
		}
		else {
			arr[j++]=ch-48;
			i++;
		}
	}
	s=0;
	for(int k=0;k<j;k++)
		s=s*10+arr[k];
	sum+=s;
	return sum;
}
int main() {
	string s;
	cin>>s;
	cout<<sum(s);
	return 0;
}
