Xth Rank - Students
The name and score of N students in a test are passed as input to the program. Also, an integer X is passed as input to the program. The program must print the student names whose rank is X with their names sorted in ascending order. If there is no such student for the given rank, the program must print -1 as the output.
Boundary Condition(s):
2 <= N <= 1000
1 <= X <= N
3 <= Length of each name <= 100
1 <= Value of each score <= 100
Input Format:
The first line contains N and X separated by a space.
The next N lines, each contains the name and the score of a student separated by a space.
Output Format:
The lines contain the student names whose rank is X with the names sorted in ascending order or the first line contains -1.
Example Input/Output 1:
Input:
6 2
peter 70
dave 86
divya 70
deepika 68
kevin 22
sherlock 68
Output:
divya
peter
Explanation:
The name and the rank of all the students are given below.
peter: Rank 2
dave: Rank 1
divya: Rank 2
deepika: Rank 4
kevin: Rank 6
sherlock: Rank 4
There are two students who got the rank 2, so their names are printed in ascending order.
Example Input/Output 2:
Input:
4 3
Shgirm 20
Mhgcx 88
Kviq 88
Hasdyg 88
Output:
-1
Explanation:
The name and the rank of all the students are given below.
Shgirm: Rank 4
Mhgcx: Rank 1
Kviq: Rank 1
Hasdyg: Rank 1
No one got the rank 3, so -1 is printed.
Java:
import java.util.*;

class ML implements CP<ML>{
    int m;
    String name;
    public int CT(ML obj){
        int v= obj.m-m;
        if(v==0){
            return name.CT(obj.name);
        }
        return v; 
    }
}
public class Hello {

    public static void main(String[] args) {
		boolean counter=true;
        Scanner scan=new Scanner(System.in);
        
        int given_number=scan.nextInt(),x=scan.nextInt();
        scan.nextLine();
        
        List<ML> list=new ArrayList<>();
        
        for(int ele=0;ele<given_number;++ele){
            String t[]=scan.nextLine().split(" ");
            int m=Integer.parseInt(t[1]);
            ML obj=new ML();
            obj.m=m;
            obj.name=t[0];
            list.add(obj);
        }
        
        Collections.sort(list);
        
        int CR=1;
        int v=1;
        for(int ele=0;ele<list.size();++ele){
            ML current=list.get(ele);
            if(ele>0){    
                ML prev=list.get(ele-1);
                if(current.m!=prev.m){
                    CR+=v;
                    v=0;
                }
                v++;
            }    
            if(CR==x){
                counter=false;
                System.out.print(current.name+"\n");
            }
        }
        if(counter)System.out.print(-1);
       
	}
}
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
    int a[1001],r[1001],n,i,j,x;
    char s[1001][1001],t[1001];
    scanf ("%d %d",&n,&x);
    for (i=0;i<n;i++)
        scanf("%s %d",s[i],&a[i]);
    for (i=0;i<n;i++)
        for(j=i+1;j<n;j++)
            if (a[i]==a[j] && strcmp(s[i],s[j])>0)
            {
                strcpy(t,s[i]);
                strcpy(s[i],s[j]);
                strcpy(s[j],t);
            }
            else if (a[i]<a[j])
            {
                strcpy(t,s[i]);
                strcpy(s[i],s[j]);
                strcpy(s[j],t);
                a[i]=a[i]^a[j];
                a[j]=a[i]^a[j];
                a[i]=a[i]^a[j];
            }
    for (i=0;i<n;i++)
    {
        r[i]=a[i];
        while (a[i]==a[i+1])
            i++;
    }
    for (i=0;i<n;i++)
        if (r[x-1]==0)
        {
            printf("-1");
            return 0;
        }
        else if (r[x-1]==a[i])
            printf("%s\n",s[i]);
}
Python:
n,k=map(int,input().split())
l=[list(input().split()) for i in range(n)]
l=sorted(l,key=lambda x:x[0])
l=sorted(l,key=lambda x:-int(x[1]))
l[0].append(1)
p=0
rank=[1]
if k==1: 
    p=1
    print(l[0][0])
for i in range(1,n):
    if l[i][1]==l[i-1][1]:
        l[i].append(l[i-1][-1])
        rank.append(l[i-1][-1])
    else:
        a=l[i-1][-1]+rank.count(l[i-1][-1]) 
        rank.append(a) 
        l[i].append(a)
    if l[i][-1]==k:
        print(l[i][0])
        p=1
if 0==p:
    print(-1)
C++:
#include <bits/stdc++.h>
#include<map>
using namespace std;

int main(int argc, char** argv)
{
    priority_queue<pair<int,string> > pq;
    map<int,int> q;
    set<string> al;
    map<int,list<pair<string,int> > > m;
    int n,x,a,z=0,y,c=0;
    string s;
    cin>>n>>x;
    for(int i=0;i<n;i++)
    {
        cin>>s>>a;
        pq.push({a,s});
    }
    while(!pq.empty())
    {
        auto w=pq.top();
        pq.pop();
        s=w.second;
        a=w.first;
        c++;
        if(m.find(a)==m.end())
        {
        m[a].push_back({s,c});
        q[c]=a;
        }
        else
        {
           for(auto vv:m[a])
           {
               m[a].push_back({s,vv.second});
               break;
           }
        }
    }
    auto e=q.find(x);
    if(e==q.end())
    cout<<"-1";
    else
    {
        int o=q[x];
        for(auto i:m[o])
        al.insert(i.first);
        while(!al.empty())
        {
            string t=*(al.begin());
            al.erase(al.begin());
            cout<<t<<endl;
        }
    }
    

}
Javascript:
var readline = require('readline');
var reader = readline.createInterface({
  input: process.stdin,
  terminal: true
});

var lines = [];

reader.on('line', function (line) {
    lines.push(line);
});

reader.on('close', function () {
    let n = lines[0].split(' ');
    let N = n[0];
    let X = n[1];
    let names = lines.slice(1);
    let Rank = [];
    for(var i=0;i<N;i++){
        var a =names[i].split(' ');
        Rank.push(parseInt(a[1]));
    }
    let rank = [1];
    var aa=1;
    Rank.sort((p,q)=>q-p);
    Rank.push(-1);
    for(var o=1;o<Rank.length;o++){
        if(Rank[o]!=Rank[o-1]){
            let ctr = rank.reduce((c,num)=>num==aa?c+1:c,0);
            aa=aa+ctr;
            rank.push(aa);
        }else{
            rank.push(aa);
        }
    }
    if(rank.includes(parseInt(X))===false){
        console.log(-1);
    }else{
        let rankHolders=[];
        let f=rank.indexOf(parseInt(X));
        let g = Rank[f];
        
        for(var j=0;j<N;j++){
            let u = names[j].split(' ');
            let Name = u[0];
            let pos = u[1];
            if(parseInt(pos)===g){
                rankHolders.push(Name);
            }
        }
        rankHolders.sort();
        for(var xx of rankHolders){
            console.log(xx);
        }
    }
});
