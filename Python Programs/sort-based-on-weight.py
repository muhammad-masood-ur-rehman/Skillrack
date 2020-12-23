Sort based on Weight
The program must accept N integers as the input. For each integer X, the program must find the sum of the weights based on the following conditions.
- If X is a perfect square then the weight is 5.
- If X is a multiple of 4 and divisible by 6 then the weight is 4.
- If X is an even integer then the weight is 3.
- Else the weight of X is 0.
The program must print the integers with their weight as the output. The integers are sorted based on their weight in ascending order. If more than one integers have the same weight then print those integers in the order of their occurrence.
Boundary Condition(s):
1 <= N <= 1000
1 <= Each integer value <= 10^4
Input Format:
The first line contains N.
The second line contains N integers separated by a space.
Output Format:
The first N lines, each contains two integers (X and their weight) based on the given conditions separated by a space.
Example Input/Output 1:
Input:
6
10 36 54 89 12 17
Output:
89 0
17 0
10 3
54 3
12 7
36 12
Explanation:
The weight of the integer 89 is 0 because it is not an even integer, not a perfect square and also not the multiple of 4 and not divisible by 6. So 89 0 are printed.
The weight of the integer 17 is 0 because it is not an even integer, not a perfect square and also not the multiple of 4 and not divisible by 6. So 17 0 are printed.
The weight of the integer 10 is 3 because it is an even integer. So 10 3 are printed.
The weight of the integer 54 is 3 because it is an even integer. So 54 3 are printed.
The weight of the integer 12 is 7 (3+4) because it is an even integer and also the multiple of 4 and divisible by 6. So 12 7 are printed.
The weight of the integer 36 is 12 (3+5+4) because it is an even integer, perfect square and also the multiple of 4 and divisible by 6. So 36 12 is printed.
Example Input/Output 2:
Input:
5
37 121 11 81 71
Output:
37 0
11 0
71 0
121 5
81 5
Python:
num,lis,s=int(input()),[],0
for ele in input().strip().split():
    w=0
    if int(ele)**0.5==int(int(ele)**0.5):
        w+=5
    if int(ele)%4==0 and int(ele)%6==0:
        w+=4
    if int(ele)%2==0:
        w+=3
    lis.append((w,int(ele)))
    if w>s:
        s=w
for foo in range(s+1):
    for bar in lis:
        if foo==bar[0]:
            print(bar[1],bar[0])
C:
#include<stdio.h>
#include <stdlib.h>

int main()
{
int num;
scanf("%d",&num);
int arra[num],weight[num],temp[8]={0,3,4,5,7,8,9,12};
for(int ele=0;ele<num;ele++)
{
    weight[ele]=0;
    scanf("%d",&arra[ele]);
    if((int)sqrt((double)arra[ele])==sqrt((double)arra[ele]))
    weight[ele]+=5;
    if(arra[ele]%4==0 && arra[ele]%6==0)
    weight[ele]+=7;
    else if(arra[ele]%2==0)
    weight[ele]+=3;
}
for(int foo=0;foo<8;foo++)
{
    for(int ele=0;ele<num;ele++)
    {
        if(weight[ele]==temp[foo])
        printf("%d %d\n",arra[ele],weight[ele]);
    }
    
}
}
C++:
#include <bits/stdc++.h>
 
using namespace std;

int main(int argc, char** argv)
{
int num,arra[1000],ele;
cin>>num;
vector<pair<int,int>> v;
for(ele=0;ele<num;ele++)
{
cin>>arra[ele];
int weight=0,temp=sqrt(arra[ele]);
if(temp*temp==arra[ele])
weight+=5;
if(arra[ele]%2==0)
{
    if(arra[ele]%4==0 && arra[ele]%6==0)
        weight+=7;
    else
        weight+=3;
}
v.push_back({weight,ele});
}
sort(v.begin(),v.end());
for(ele=0;ele<num;ele++)
cout<<arra[v[ele].second]<<" "<<v[ele].first<<endl;
}
Java:
#include<stdio.h>
#include <stdlib.h>
struct Box{
    int val;
    int weight;
};
int isPerfectSquare(int n){
    return ((int)sqrt(n)*(int)sqrt(n)) ==n ;
}
int cmp(const void* obj1,const void* obj2){
    struct Box* b1=(struct Box*)obj1;
    struct Box* b2=(struct Box*)obj2;
    int var=b1->weight - b2->weight;
    return var;
}
int main()
{
    int n;
    scanf("%d",&n);
    struct Box arr[n];
    
    for(int i=0;i<n;++i){
        int num;
        int wt=0;
        scanf("%d",&num);
        
        if(isPerfectSquare(num))wt+=5;
        if(num%4==0 && num%6==0)wt+=4;
        if(num%2==0)wt+=3;
        
        struct Box obj;
        obj.val=num;
        obj.weight=wt;
        arr[i]=obj;
    }
    qsort(arr,n,sizeof(struct Box),cmp);
    
    for(int i=0;i<n;++i)printf("%d %d\n",arr[i].val,arr[i].weight);
}
