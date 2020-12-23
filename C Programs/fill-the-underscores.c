Fill the Underscores
The program must accept a string S containing underscore(s) and N string values as the input. A group of consecutive underscores in the string S is called a slot. The program must print the number of slots in the string S that can be filled with the given N string values. A slot can be filled with a string only if the length of the slot is equal to the length of the string. A string can not be used to fill two or more slots.
Note: The string S contains at least 1 underscore.
Boundary Condition(s):
1 <= N <= 100
1 <= Length of each string (including S) <= 1000
Input Format:
The first line contains S.
The second line contains N.
The next N lines, each contains a string.
Output Format:
The first line contains an integer representing the number of slots in the string S that can be filled with the given N string values.
Example Input/Output 1:
Input:
skill____programming________
5
hardworking
rack
good
platform
developement
Output:
2
Explanation:
Here S = skill____programming________
There are 2 slots in the string S and their lengths are 4 and 8.
The first slot can be filled with rack or good.
The second slot can be filled with platform.
Here both the slots are filled with the string values as per the given conditions.
Hence the output is 2
Example Input/Output 2:
Input:
cat___lion___tiger________Panda__________
6
Ox
Cat
Mouse
Emu
Elephant
Monkey
Output:
3
Example Input/Output 3:
Input:
#__Apples#__bananas
4
100
12
5000
875
Output:
1
Python:
import re
s=input().strip().lower()
s1=re.split('[a-z#!$@&*)(%+-?]',s)
l=[]
for i in s1:
    if i!='':
        l.append(len(i))
c=0
n=int(input())
for i in range(0,n):
    x=input().strip()
    if len(x) in l:
        c=c+1
        l.remove(len(x))
print(c)
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int n,slot_num = 0,slot_count[10001],result = 0;
    char word[1001];
    scanf("%s\n%d",word,&n);
    for(int i = 0;i < strlen(word);i++)
    {
        if(word[i] == '_')
        {
            int count = 0,j = 0;
            for(j = i ; word[j] == '_' ;j++)
            {
                count++;
            }
            slot_count[slot_num++] = count;
            i = j-1;
        }
    }
    for(int i = 0;i < n;i++)
    {
        char fillers[1001];
        scanf("%s\n",fillers);
        int length = strlen(fillers);
        for(int i = 0;i < slot_num;i++)
        {
            if(length == slot_count[i])
            {result++;slot_count[i] = 0;break;}
        }
        if(slot_num == result)
        break;
    }
    printf("%d",result);
}
C++:
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char** argv)
{
string s;
getline(cin, s);
int n;
cin >> n;
vector<int> v;
vector<int> :: iterator it;
for(int i=0; i<n; i++)
{
    string str;
    cin >> str;
    v.push_back(str.length());
}
int  res = 0;
for(int i=0; i<s.length(); i++)
{
    int c = 0;
    while(s[i] == '_')
    {
        i++;
        c++;
    }
    
    it = std::find(v.begin(), v.end(), c);
    if(it != v.end())
    {
        res++;
        v.erase(it);
    }
}

cout <<  res; 
}
Java:
import java.util.*;
import java.util.regex.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String s=sc.nextLine();
		int a=sc.nextInt();
		List<Integer> al=new ArrayList<>();
		List<String> al2=new ArrayList<>();
		String []arr=new String[a];
		for(int i=0;i<a;i++)
		{
		    arr[i]=sc.next();
		    al2.add(arr[i]);
		}
		Pattern p=Pattern.compile("[_]+");
		Matcher m=p.matcher(s);
		while(m.find())
		{
		   String str=m.group();
		   int len=str.length();
		   al.add(len);
		}
		int count=0;
		for(int i=0;i<al.size();i++)
		{
		    for(int j=0;j<al2.size();j++)
		    {
		        String st=al2.get(j);
		        int l=st.length();
		        if(al.get(i)==l)
		        {
		            count++;
		            al2.remove(j);
		            break;
		        }
		    }
		    
		}
		System.out.println(count);
		
	}
}
