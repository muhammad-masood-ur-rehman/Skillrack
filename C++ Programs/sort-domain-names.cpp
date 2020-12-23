Sort - Domain Names
The program must accept the email addresses of N students as the input. The program must print the names of the email domains based on the usage count(most used domains to least used domains) in the given N email addresses. If more than one domains have the same usage count, then those domain names must be sorted in ascending order.
Boundary Condition(s):
2 <= N <= 100
10 <= Length of each email address <= 50
Input Format:
The first line contains N.
The next N lines, each contains an email address.
Output Format:
The lines contain the email domain names as per the given conditions.
Example Input/Output 1:
Input:
5
abc@gmail.com
koolguy@yahoo.com
mno@gmail.com
manjara@gmail.com
haven@live.com
output:
gmail.com
live.com
yahoo.com
Explanation:
3 students have the email addresses at "gmail.com".
1 student has the email address at "live.com".
1 student has the email address at "yahoo.com".
The most used domain name is gmail.com, so it is printed first.
The domains yahoo.com and live.com have the same usage count, so their names are printed in ascending order.
Example Input/Output 2:
Input:
5
xyz@gmail.com
fun4ever@outlook.com
sweetcandy@yahoo.com
mrabc@gmail.com
comichero@live.com
Output:
gmail.com
live.com
outlook.com
yahoo.com
Example Input/Output 3:
Input:
4
AtoZ@gmail.com
viten123@rocketmail.com
HELLOMR@live.com
Master@outlook.com
Output:
gmail.com
live.com
outlook.com
rocketmail.com
Python:
n=int(input())
l=[]
for i in range(n):
    s=input().split('@')
    l.append(s[1].strip())
a=list(set(l))
a.sort(reverse=True)
a.sort(key=lambda x:l.count(x))
print(*a[::-1],sep='\n')
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
char s[101][51],l[51];
int i,j,n,h[101]={0},c,t;
scanf("%d ",&n);
for(i=0;i<n;i++)
scanf("%[^@]@%s ",l,s[i]);
for(i=0;i<n;i++)
if(s[i][0]!='*'){
c=1;
for(j=i+1;j<n;j++)
if(strcmp(s[i],s[j])==0)
{
    c++;
    s[j][0]='*';
}
h[i]=c;
}
for(i=0;i<n;i++)
for(j=i+1;j<n;j++)
if(h[i]<h[j]||(h[i]==h[j]&&strcmp(s[i],s[j])>0))
{
    strcpy(l,s[i]);
    strcpy(s[i],s[j]);
    strcpy(s[j],l);
    t=h[i],h[i]=h[j],h[j]=t;
}
for(i=0;i<n;i++)
if(s[i][0]!='*')
printf("%s\n",s[i]);
}
C++:
#include <bits/stdc++.h>
using namespace std;
bool comp(pair<int,string> x,pair<int,string> y){
    if(x.first>y.first)
        return true;
    if(x.first<y.first)
        return false;
    else{
        if(x.second<y.second)
            return true;
        else
            return false;
    }
}
int main(int argc, char** argv)
{
    int n;
    cin>>n;
    string s;
    map <string,int> m;
    for(int i=0;i<n;i++){
        cin>>s;
        stringstream iss(s);
        string temp;
        vector <string> v;
        while(getline(iss,temp,'@')){
            v.push_back(temp);
        }
        m[v[1]]++;
    }    
    vector<pair<int,string>> res;
    for(auto it=m.begin();it!=m.end();it++)
    {
        res.push_back(make_pair(it->second,it->first));
    }
    sort(res.begin(),res.end(),comp);
    for(auto x:res)
        cout<<x.second<<endl;
}
Java:
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		//Your Code Here
	 Scanner sc=new Scanner(System.in);
	 Map<String,Integer> map=new TreeMap<>();
	 int n=sc.nextInt();
	 int max=0;
	 for(int i=0;i<n;i++){
	     String[] s=sc.next().split("@");
	    if(!map.containsKey(s[1]))
	    map.put(s[1],1);
	    else
	    map.put(s[1],map.get(s[1])+1);
	    if(max<map.get(s[1]))
	    max=map.get(s[1]);
	 }
	 while(max>0){
	  for(Map.Entry i:map.entrySet()){
	      int val=(int)(i.getValue());
	      if(val==max)
	  System.out.println(i.getKey());
	  }
	  max--;
	 }

	}
}
